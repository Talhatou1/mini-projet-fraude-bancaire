# 💳 Analyse exploratoire des transactions bancaires (fraude)

Ce projet consiste à analyser un jeu de données réel contenant plus de **284 000 transactions bancaires**, dont seulement **0.17%** sont frauduleuses.  
L’objectif principal est de comprendre la structure du dataset, d’étudier les variables importantes et d’identifier les patterns liés à la fraude.

---

## 📁 Structure du projet

Mini-projet
┣ 📂 app/ → Application Streamlit
┃ ┗ 📄 app.py
┣ 📂 data/ → Jeu de données
┃ ┗ 📄 creditcard.csv
┣ 📂 notebook/ → Notebook d’analyse
┃ ┗ 📄 EDA_fraude.ipynb
┣ 📄 README.md
┗ 📄 requirements.txt


---

## 🎯 Objectifs du projet

- Explorer et comprendre le dataset  
- Analyser la répartition des transactions frauduleuses  
- Étudier les variables : **Amount**, **Time**, **V1–V28 (PCA)**  
- Identifier les variables les plus corrélées avec la fraude  
- Créer des visualisations (Matplotlib, Seaborn, Plotly)  
- Développer une **application Streamlit interactive**  
- Produire un **rapport PDF** résumant les résultats  

---

## 📊 Contenu du notebook (`EDA_fraude.ipynb`)

### ✔ 1. Aperçu général
- Chargement des données  
- Types des variables  
- Valeurs manquantes  
- Statistiques descriptives  

### ✔ 2. Analyse de la variable *Class*
- Comptage des transactions normales vs frauduleuses  
- Visualisation du déséquilibre (countplot)  

### ✔ 3. Analyse du montant (`Amount`)
- Histogrammes  
- Boxplots  
- Comparaison entre classes  

### ✔ 4. Analyse temporelle (`Time`)
- Distribution du temps  
- Time vs Amount  
- Comparaison selon la classe  

### ✔ 5. Corrélations
- Matrice de corrélation  
- Heatmap (Seaborn + Plotly)  
- Variables les plus corrélées avec la fraude  

### ✔ 6. Visualisations avancées
- Boxplots pour les variables importantes  
- Scatterplots (V10, V12, V14, V17…)  
- Densités KDE  

---

## 🌐 Application Streamlit

Une application interactive a été développée dans le dossier `app/`.

### ▶️ Lancer l'application :

```bash
cd app
streamlit run app.py

Fonctionnalités :

    Visualisation interactive du dataset

    Analyse du montant et du temps

    Corrélations (Plotly)

    Filtrage par classe (fraude / normal)

⚙️ Installation du projet
1️⃣ Créer un environnement virtuel

python -m venv .venv

2️⃣ Activer l’environnement

Windows :

.venv\Scripts\activate

Mac / Linux :

source .venv/bin/activate

3️⃣ Installer les dépendances

pip install -r requirements.txt

4️⃣ Ouvrir le notebook

jupyter notebook

📚 Description du dataset

    V1 à V28 : composantes PCA

    Amount : montant de la transaction

    Time : temps écoulé depuis la première transaction

    Class :

        0 → transaction normale

        1 → transaction frauduleuse

🔮 Améliorations possibles

    Rééquilibrage des données (SMOTE)

    Modèles de classification (XGBoost, Random Forest, SVM…)

    Sélection automatique des variables

    Dashboard Streamlit plus complet



