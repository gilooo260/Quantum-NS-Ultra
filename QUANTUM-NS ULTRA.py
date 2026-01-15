import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
import plotly.graph_objects as go
import pandas as pd
import io
import re
from sklearn.preprocessing import StandardScaler

# =================================================================
# 1. MOTEUR DE GÉNÉRATION DE DONNÉES (THÉORIE & RÉEL)
# =================================================================

class QuantumDataEngine:
    """Générateur vectorisé haute performance et pont de données réelles."""
    
    @staticmethod
    def generate_theory_data(n_samples=5000, n_points=128):
        """Génère des milliers de simulations en quelques millisecondes."""
        t = np.linspace(0, 1, n_points)
        T = np.tile(t, (n_samples, 1))
        nu = np.random.uniform(1e-4, 1e-2, (n_samples, 1))
        knot_types = np.random.randint(0, 4, n_samples)
        
        X, Y, Z = np.zeros_like(T), np.zeros_like(T), np.zeros_like(T)
        
        for kt in range(4):
            idx = (knot_types == kt)
            if not np.any(idx): continue
            q = np.exp(2j * np.pi * T[idx])
            if kt == 0: # Trefoil
                X[idx], Y[idx] = np.real(q * (1 + q**3)), np.imag(q * (1 + q**3))
                Z[idx] = np.real(q**2)
            elif kt == 1: # Figure Eight
                val = q + q**(-1) - q**2 - q**(-2)
                X[idx], Y[idx], Z[idx] = np.real(val), np.imag(val), np.real(q**3)
            elif kt == 2: # Cinquefoil
                X[idx], Y[idx] = np.real(q * (1 + q**5)), np.imag(q * (1 + q**5))
                Z[idx] = np.real(q**3 - q**2)
            else: # Torus
                theta = 2 * np.pi * T[idx]
                X[idx] = (2 + np.cos(3*theta)) * np.cos(2*theta)
                Y[idx] = (2 + np.cos(3*theta)) * np.sin(2*theta)
                Z[idx] = np.sin(3*theta)

        # Physique simplifiée : Calcul de la vorticité (Label cible)
        v = np.sqrt(np.gradient(X, axis=1)**2 + np.gradient(Y, axis=1)**2)
        omega_max = np.max(np.abs(np.gradient(v, axis=1)), axis=1) / (nu.flatten() * 100)
        
        features = np.stack([
            np.mean(v, axis=1), np.std(v, axis=1), 
            np.max(v, axis=1), nu.flatten(),
            knot_types.astype(float)
        ], axis=1)
        
        return features, omega_max.reshape(-1, 1), (X, Y, Z)

    @staticmethod
    def convert_raw_to_csv(input_path, output_path):
        """Convertit des fichiers bruts CFD (dat/txt) en CSV structuré."""
        with open(input_path, 'r') as f:
            lines = [re.sub(r'\s+', ',', l.strip()) for l in f if l.strip() and not l.startswith(('#', '%'))]
        df = pd.read_csv(io.StringIO("\n".join(lines)), names=['x', 'y', 'z', 'ux', 'uy', 'uz', 'p'])
        df['viscosity'] = 1.0e-6 # Valeur par défaut
        df['knot_type'] = 0
        df.to_csv(output_path, index=False)
        return df

# =================================================================
# 2. ARCHITECTURE IA : PHYSICS-INFORMED RESNET
# =================================================================

class PhysicsResNet(nn.Module):
    """Architecture profonde avec connexions résiduelles (Skip Connections)."""
    def __init__(self, input_dim=5):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, 256)
        self.bn1 = nn.BatchNorm1d(256)
        
        # Bloc Résiduel
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 256)
        self.bn2 = nn.BatchNorm1d(256)
        
        self.head = nn.Linear(256, 1)
        self.dropout = nn.Dropout(0.1)

    def forward(self, x):
        x = F.silu(self.bn1(self.fc1(x))) # Activation SiLU (Swish)
        identity = x
        out = F.silu(self.bn2(self.fc2(x)))
        out = self.fc3(out)
        out += identity # Fusion de l'information (ResNet)
        return self.head(self.dropout(F.silu(out)))

# =================================================================
# 3. VISUALISATION & PIPELINE PRINCIPAL
# =================================================================

def visualize_knot(X, Y, Z, index=0):
    """Affiche le filament de vortex en 3D."""
    fig = go.Figure(data=[go.Scatter3d(
        x=X[index], y=Y[index], z=Z[index],
        mode='lines', line=dict(color='gold', width=7)
    )])
    fig.update_layout(title="Topologie du Vortex Quantique", template="plotly_dark")
    fig.show()

def main():
    print("🚀 Initialisation de QUANTUM-NS ULTRA...")
    
    # --- ÉTAPE 1 : Données ---
    engine = QuantumDataEngine()
    features, labels, coords = engine.generate_theory_data(n_samples=10000)
    X_c, Y_c, Z_c = coords
    
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    # --- ÉTAPE 2 : Modèle ---
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = PhysicsResNet(input_dim=5).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
    
    X_train = torch.FloatTensor(features_scaled).to(device)
    y_train = torch.FloatTensor(labels).to(device)

    # --- ÉTAPE 3 : Entraînement avec perte physique ---
    print(f"🧠 Entraînement du Physics-ResNet sur {device}...")
    model.train()
    for epoch in range(101):
        optimizer.zero_grad()
        pred = model(X_train)
        
        # Perte Hybride : Précision (MSE) + Physique (Positivité)
        loss_mse = F.mse_loss(pred, y_train)
        loss_phys = F.relu(-pred).mean() # Pénalise les prédictions négatives impossibles
        total_loss = loss_mse + 0.5 * loss_phys
        
        total_loss.backward()
        optimizer.step()
        
        if epoch % 20 == 0:
            print(f"   Epoch {epoch:3d} | Loss: {total_loss.item():.6f}")

    # --- ÉTAPE 4 : Visualisation ---
    print("📊 Génération de la vue 3D...")
    visualize_knot(X_c, Y_c, Z_c, index=np.random.randint(0, 10000))
    print("✅ Simulation et entraînement terminés.")

if __name__ == "__main__":
    main()