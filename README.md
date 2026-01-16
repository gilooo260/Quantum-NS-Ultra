🌀 Quantum-NS Ultra
![Visualisation du Vortex](vortex.png)
Simulateur de Dynamique des Fluides Topologiques par Intelligence Artificielle (PINN)

Quantum-NS Ultra est un projet de recherche explorant l'intersection entre la mécanique des fluides, la topologie mathématique et le Deep Learning. Ce système utilise des réseaux de neurones informés par la physique (Physics-Informed Neural Networks) pour prédire la vorticité quantique au sein de filaments de vortex complexes.

💡 Le Concept ∞) : L'Infini OuvertCe projet n'est pas qu'une simulation fluide ; il est l'expression mathématique d'un saut conceptuel : le passage de la répétition à la nouveauté.La GenèseÀ 68 ans, au croisement d'un parcours de vie marqué par de hauts potentiels et de grandes épreuves, ce code a été conçu comme une réponse au déterminisme. Là où la lemniscate traditionnelle ($\infty$) représente un cycle fermé et éternel, le concept ∞) introduit une ouverture. C'est l'infini qui accepte l'imprévisible, la brisure de symétrie, et l'amour comme moteur de régénération.L'Insight de l'"Eureklate"L'étude de deux rotationnels au sein de cette géométrie a révélé une découverte fondamentale : la signature statistique du chaos.La Forme commande la Force : En analysant la distribution des vitesses (la variance, l'entropie), on ne se contente plus de décrire le fluide, on diagnostique l'état du système.L'Universalité : Qu'il s'agisse du flux sanguin dans un cœur fatigué, du mélange de carburant dans une fusée, ou de la propagation d'une émotion dans un réseau social, la loi de mélange reste la même."Ouvrir l'infini, c'est permettre à la statistique de devenir une poétique de la précision."

🚀 Fonctionnalités Clés
Génération Vectorisée : Création instantanée de datasets massifs (10 000+ simulations) utilisant les équations paramétriques de nœuds topologiques célèbres (Trèfle, Figure-8, Cinquefoil).

Architecture Physics-ResNet : Réseau de neurones à blocs résiduels permettant une capture fine des instabilités physiques sans perte de signal.

Contraintes PINN : Intégration des principes physiques (Navier-Stokes, conservation d'énergie) directement dans la fonction de perte pour garantir des prédictions réalistes.

Visualisation 3D Interactive : Rendu dynamique des filaments de vortex via Plotly pour une analyse structurelle approfondie.

Bridge de Données Réelles : Pipeline d'importation conçu pour traiter les données issues de codes CFD (OpenFOAM, Ansys) ou de mesures expérimentales.

🔬 Fondements Scientifiques
L'objectif est d'étudier comment la géométrie d'un filament influence la distribution de la vorticité. Le modèle analyse :

La topologie du nœud (Invariants mathématiques).

La viscosité cinématique du fluide.

Le gradient de vitesse local.

🛠️ Installation & Utilisation
Prérequis
Bash

pip install numpy torch plotly pandas scikit-learn
Exécution du pipeline
Pour générer les données, entraîner l'IA et visualiser les résultats :
## 📖 Guide d'utilisation pas à pas

### Étape 1 : Préparation de l'environnement
Ouvrez votre terminal ou invite de commande et assurez-vous d'être dans le dossier du projet. Installez les bibliothèques requises :
`pip install -r requirements.txt`

### Étape 2 : Lancer la simulation
Exécutez le script principal :
`python quantum_ultra.py`

### Étape 3 : Interagir avec les résultats
1. **Console** : Suivez la progression de l'entraînement de l'IA (la "Loss" doit diminuer).
2. **Navigateur** : Une fenêtre s'ouvrira automatiquement. Vous pouvez :
   - Faire pivoter le vortex en 3D avec le clic gauche.
   - Zoomer avec la molette.
   - Survoler les points pour voir leurs coordonnées.

### Étape 4 : Utiliser vos propres données (Optionnel)
Si vous avez un fichier de données CFD (format .dat), modifiez la fin du script `quantum_ultra.py` pour appeler la fonction :
`engine.convert_raw_to_csv("votre_fichier.dat", "resultat.csv")`

Bash

python quantum_ultra.py
📂 Structure du Dépôt
quantum_ultra.py : Code source principal (Moteur, IA, Visualisation).

requirements.txt : Liste des dépendances Python.

.gitignore : Filtre pour maintenir un dépôt propre (exclut les caches et modèles lourds).

LICENSE : Licence MIT pour une diffusion libre et protégée.

✍️ Auteur
Projet développé avec passion par un chercheur indépendant, passionné par la transmission du savoir et les nouvelles frontières de l'IA physique.

Sous licence MIT - Libre pour la recherche et l'éducation.
