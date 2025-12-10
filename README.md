💳 Analyse Exploratoire d’un Jeu de Données Bancaires – Détection de Fraude

Projet – Outils de programmation pour la science des données
Université du Québec à Chicoutimi (UQAC)

📌 Description générale

Ce projet consiste à réaliser une analyse exploratoire complète (EDA) d’un jeu de données réel contenant 284 807 transactions bancaires, dont 492 fraudeuses.
L’objectif est de :

comprendre la structure du dataset,

analyser les variables (Time, Amount, V1–V28),

mettre en évidence le déséquilibre des classes,

visualiser les tendances importantes,

créer une application Streamlit interactive capable d’afficher, filtrer et explorer les données.

Aucun modèle de prédiction n’est demandé : il s’agit uniquement d’un travail exploratoire structuré.

📁 Structure du projet
mini-projet-fraude-bancaire/
│
├── app/
│   └── app.py                  # Application Streamlit
│
├── data/
│   └── creditcard.csv          # Téléchargé automatiquement via Google Drive au premier lancement
│
├── notebook/
│   └── EDA_fraude.ipynb        # Analyse exploratoire complète (EDA)
│
├── requirements.txt            # Dépendances du projet
└── README.md                   # Documentation du projet

🔍 Contenu du fichier creditcard.csv

Le dataset contient :

Colonne	Description
Time	Temps écoulé depuis la première transaction
Amount	Montant de la transaction
V1–V28	Variables dérivées d’une transformation PCA
Class	0 = normale, 1 = fraude

Le fichier original est trop volumineux pour être stocké directement sur GitHub.
➡️ Il est donc téléchargé automatiquement via Google Drive lors du premier lancement de l'application Streamlit.

🚀 Application Streamlit

L'application permet de :

afficher un résumé du dataset (nombre de transactions, de fraudes, pourcentage)

explorer la répartition des classes

analyser les variables Amount et Time

générer des graphiques interactifs (Plotly)

afficher une carte thermique de corrélations

filtrer les transactions normales ou frauduleuses

🌐 Téléchargement automatique du dataset (Google Drive)

Le fichier complet creditcard.csv est hébergé sur Google Drive.
L'application utilise gdown pour :

vérifier si le fichier existe localement,

sinon le télécharger automatiquement,

puis le charger avec pandas.

file_id = "14xAlw2F-drxaG137tiFF4xDIGRnY6F1n"
gdown.download(id=file_id, output="data/creditcard.csv", quiet=False)


Cela permet d'exécuter l’application même sans inclure le fichier CSV dans le dépôt GitHub.

🧪 Analyse exploratoire (EDA) – Notebook

Le notebook EDA_fraude.ipynb contient :

1️⃣ Chargement et exploration du dataset

dimensions

types

valeurs manquantes

statistiques descriptives

2️⃣ Analyse des distributions

Histogrammes et boxplots de Amount

Analyse temporelle avec Time

3️⃣ Analyse de la variable cible

Comptage des classes

Visualisation du déséquilibre

4️⃣ Corrélations et relations

Matrice de corrélation

Heatmap

Variables les plus liées à la fraude (ex : V10, V12, V14…)

5️⃣ Visualisations supplémentaires

Scatterplots

Distributions selon la classe

6️⃣ Synthèse des observations

Résumé clair des patterns observés.

⚙️ Installation et exécution
📥 1. Cloner le projet
git clone https://github.com/ton-repo/mini-projet-fraude-bancaire.git
cd mini-projet-fraude-bancaire

🧩 2. Créer et activer un environnement virtuel
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.\.venv\Scripts\activate       # Windows

📦 3. Installer les dépendances
pip install -r requirements.txt

▶️ 4. Lancer l'application Streamlit
streamlit run app/app.py


Au premier lancement, creditcard.csv sera téléchargé automatiquement depuis Google Drive.

📊 Technologies utilisées

Python 3.x

Pandas – manipulation de données

NumPy – calculs numériques

Matplotlib / Seaborn – visualisations classiques

Plotly – visualisations interactives

Streamlit – application web

gdown – téléchargement Google Drive

👩‍💻 Auteur

Talhatou Baldé
Baccalauréat en informatique
Université du Québec à Chicoutimi (UQAC)

📌 Remarque importante

Ce projet a été réalisé dans un cadre académique et ne doit pas être utilisé pour des systèmes réels de détection de fraude.

🎉 Merci d’avoir consulté ce projet !

N’hésitez pas à ouvrir une issue ou un pull request sur GitHub si vous souhaitez proposer des améliorations.