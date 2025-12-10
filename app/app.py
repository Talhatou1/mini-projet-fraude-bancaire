import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import os
import gdown


# =========================
# Configuration générale de la page
# =========================
st.set_page_config(
    page_title="Analyse exploratoire - Fraude bancaire",
    page_icon="💳",
    layout="wide"
)

# =========================
# Chargement des données
# =========================
@st.cache_data
def load_data():
    # Chemin local où sera stocké le fichier téléchargé
    local_path = "data/creditcard.csv"
    os.makedirs("data", exist_ok=True)

    # Si le fichier n'existe pas encore sur le serveur, on le télécharge depuis Google Drive
    if not os.path.exists(local_path):
        file_id = "14xAlw2F-drxaG137tiFF4xDIGRnY6F1n"
          # ton ID Google Drive
        url = f"https://drive.google.com/file/d/14xAlw2F-drxaG137tiFF4xDIGRnY6F1n/view?usp=drive_link"

        # Téléchargement avec gdown
        gdown.download(url, local_path, quiet=False)

    # Lecture du CSV complet en local
    df = pd.read_csv(local_path)
    return df




df = load_data()

# =========================
# Barre latérale (options)
# =========================
st.sidebar.title("⚙️ Options d’affichage")

classe_option = st.sidebar.selectbox(
    "Filtrer les données pour les graphiques :",
    options=[
        "Toutes les transactions",
        "Transactions normales (Class = 0)",
        "Transactions frauduleuses (Class = 1)"
    ]
)

df_filtered = df.copy()
if classe_option == "Transactions normales (Class = 0)":
    df_filtered = df_filtered[df_filtered["Class"] == 0]
elif classe_option == "Transactions frauduleuses (Class = 1)":
    df_filtered = df_filtered[df_filtered["Class"] == 1]

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Info :** le filtre s’applique aux graphiques des sections 3 et 4 "
    "(montant et temps), mais le résumé global reste sur l’ensemble du dataset."
)

# =========================
# Titre et introduction
# =========================
st.title("💳 Analyse exploratoire des transactions bancaires")

st.write(
    """
    Cette application présente une **analyse exploratoire (EDA)** d'un jeu de données 
    réelles de transactions bancaires comprenant des transactions **frauduleuses** et 
    **non frauduleuses**. Utilisez la barre latérale pour régler les options d'affichage.
    """
)

st.markdown("---")

# ============================================================
# 1. Résumé du jeu de données
# ============================================================
st.header("1. Résumé du jeu de données")

col1, col2, col3 = st.columns(3)

nb_total = len(df)
nb_fraudes = df["Class"].sum()
pct_fraudes = nb_fraudes / nb_total * 100

with col1:
    st.metric("Nombre total de transactions", f"{nb_total:,}".replace(",", " "))
with col2:
    st.metric("Nombre de fraudes", f"{nb_fraudes:,}".replace(",", " "))
with col3:
    st.metric("Pourcentage de fraudes", f"{pct_fraudes:.3f} %")

st.subheader("Aperçu des premières lignes du jeu de données :")
st.dataframe(df.head())

st.markdown("---")

# ============================================================
# 2. Répartition des classes (fraude vs non-fraude)
# ============================================================
st.header("2. Répartition des classes (fraude vs non-fraude)")

class_counts = df["Class"].value_counts().sort_index()
class_labels = {0: "Normal", 1: "Fraude"}
class_counts_named = class_counts.rename(index=class_labels)

fig_class = px.bar(
    class_counts_named,
    x=class_counts_named.index,
    y=class_counts_named.values,
    labels={"x": "Classe", "y": "Nombre de transactions"},
    title="Nombre de transactions par classe"
)
fig_class.update_layout(showlegend=False)

st.plotly_chart(fig_class, use_container_width=True)

st.markdown(
    """
    👉 On constate un **déséquilibre très important** : la majorité des transactions sont 
    normales (classe 0), et la fraude (classe 1) représente une proportion très faible.
    """
)

st.markdown("---")

# ============================================================
# 3. Analyse du montant des transactions (Amount)
# ============================================================
st.header("3. Analyse du montant des transactions (Amount)")

st.markdown(f"**Filtre actuel pour les graphiques :** _{classe_option}_")

col_left, col_right = st.columns(2)

# On travaille sur df_filtered ici
if len(df_filtered) == 0:
    st.warning("Aucune donnée pour le filtre sélectionné.")
else:
    # Histogramme global du montant
    with col_left:
        st.subheader("Histogramme du montant")
        fig_amount = px.histogram(
            df_filtered,
            x="Amount",
            nbins=50,
            title="Distribution du montant des transactions",
            labels={"Amount": "Montant"}
        )
        st.plotly_chart(fig_amount, use_container_width=True)

    # Histogramme du montant par classe (si plusieurs classes présentes)
    with col_right:
        st.subheader("Histogramme du montant par classe")
        fig_amount_class = px.histogram(
            df_filtered,
            x="Amount",
            color="Class",
            nbins=50,
            barmode="overlay",
            title="Montant des transactions selon la classe",
            labels={"Amount": "Montant", "Class": "Classe"}
        )
        fig_amount_class.update_traces(opacity=0.6)
        st.plotly_chart(fig_amount_class, use_container_width=True)

    st.markdown(
        """
        👉 La majorité des transactions portent sur de **petits montants**, 
        avec quelques montants très élevés qui apparaissent comme des **valeurs extrêmes**.
        """
    )

st.markdown("---")

# ============================================================
# 4. Temps des transactions et corrélations
# ============================================================
st.header("4. Temps des transactions et corrélations")

col_scatter, col_corr = st.columns(2)

# ---------------- Scatter Time vs Amount (avec filtre)
with col_scatter:
    st.subheader("Temps vs montant (échantillon)")

    if len(df_filtered) > 0:
        # Échantillon pour ne pas surcharger le graphique
        n_sample = min(10000, len(df_filtered))
        df_sample = df_filtered.sample(n_sample, random_state=42) if len(df_filtered) > n_sample else df_filtered

        fig_scatter = px.scatter(
            df_sample,
            x="Time",
            y="Amount",
            color="Class",
            title="Montant des transactions en fonction du temps",
            labels={"Time": "Temps (s)", "Amount": "Montant", "Class": "Classe"},
            opacity=0.6
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Impossible d'afficher le nuage de points : aucune donnée pour le filtre choisi.")

# ---------------- Heatmap des corrélations (sur tout le dataset)
with col_corr:
    st.subheader("Carte thermique des corrélations")

    # Corrélation sur toutes les variables numériques (dataset complet)
    corr = df.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr,
        cmap="Blues",
        ax=ax,
        cbar_kws={"label": "Corrélation"},
        xticklabels=False,  # pour alléger l’affichage
    )
    ax.set_title("Matrice de corrélation des variables")
    st.pyplot(fig)

st.markdown(
    """
    👉 Certaines composantes (par exemple **V10, V12, V14, V17...**) montrent des corrélations 
    plus fortes avec la variable **Class**, ce qui pourra être exploité lors d'un futur travail de 
    **modélisation**.
    """
)

st.info(
    "ℹ️ Les variables **V1–V28** proviennent d'une transformation **PCA** : "
    "elles ne sont pas directement interprétables mais capturent des combinaisons de variables originales."
)
