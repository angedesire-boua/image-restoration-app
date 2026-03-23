import cv2
import numpy as np
from PIL import Image
import streamlit as st
from io import BytesIO
import os

# Titre et description
st.title("🖼️ Mini Projet : Restauration d'Image ")
st.write("""
Ce mini projet s’inscrit dans le cadre du cours de traitement d’image. Il vise à améliorer la qualité visuelle d’images dégradées,
et illustre des applications concrètes dans des domaines sensibles comme la santé, la justice ou la conservation d’archives.
""")

# Image d'exemple affichée uniquement à titre illustratif
st.markdown("### 📌 Exemple illustratif")
exemple_path = "images/exemple.jpg"
if os.path.exists(exemple_path):
    st.image(exemple_path, caption="Exemple visuel (non traité)", use_container_width=True)
else:
    st.warning("⚠️ L'image d'exemple est introuvable.")

# Facultatif : rappel de l'encart impact
with st.expander("🌍 Impact concret de la restauration d’image (rappel)"):
    st.markdown("""
La restauration d'image joue un rôle crucial dans plusieurs domaines :

- 🏛️ **Archivage historique**
- ⚖️ **Justice & criminalistique**
- 🏥 **Médical**
- 🧠 **IA & reconnaissance visuelle**
    """)

# Téléversement de l'image
uploaded_file = st.file_uploader("📤 Téléverse une image (jpg, png)", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
else:
    if os.path.exists(exemple_path):
        img = cv2.imread(exemple_path, cv2.IMREAD_COLOR)
        st.info("✅ Aucune image téléversée. Utilisation de l'image par défaut.")
    else:
        st.error("❌ Aucune image fournie et l'image par défaut est absente.")
        st.stop()

# Conversion en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Choix du filtre
st.markdown("### 🎛️ Filtrage de l'image")
filter_type = st.selectbox("Choisis un filtre de réduction de bruit :", ["Gaussien", "Médian", "Bilatéral"])

if filter_type == "Gaussien":
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)
elif filter_type == "Médian":
    denoised = cv2.medianBlur(gray, 5)
else:  # Bilatéral
    denoised = cv2.bilateralFilter(gray, 9, 75, 75)

# Réglage de la netteté
sharpness_factor = st.slider("🔧 Intensité de la netteté", 0.0, 2.0, 1.2, 0.1)

# Appliquer filtre Laplacien
laplacian = cv2.Laplacian(denoised, cv2.CV_64F)
sharpened = cv2.convertScaleAbs(denoised - sharpness_factor * laplacian)

# Optionnel : égalisation d'histogramme
apply_contrast = st.checkbox("✨ Rehausser automatiquement le contraste", value=True)
if apply_contrast:
    sharpened = cv2.equalizeHist(sharpened)

# Affichage côte-à-côte
st.markdown("### 🖼️ Résultats Visuels")
col1, col2 = st.columns(2)
with col1:
    st.image(gray, caption="🟠 Image originale (niveaux de gris)", use_container_width=True)
with col2:
    st.image(sharpened, caption=f"🟢 Image restaurée ({filter_type})", use_container_width=True)

# Détails des traitements
with st.expander("📋 Voir les étapes techniques appliquées"):
    st.markdown(f"""
    - 🔄 Conversion en niveaux de gris.
    - 🧹 Réduction du bruit avec le filtre **{filter_type}**.
    - ✨ Netteté renforcée (facteur : {sharpness_factor}).
    - 📊 {"Égalisation du contraste activée." if apply_contrast else "Pas d’égalisation du contraste."}
    """)

# Téléchargement de l'image restaurée
restored_pil = Image.fromarray(sharpened)
buf = BytesIO()
restored_pil.save(buf, format="PNG")
byte_im = buf.getvalue()

st.download_button(
    label="📥 Télécharger l’image restaurée",
    data=byte_im,
    file_name="image_restauree.png",
    mime="image/png"
)

# Pied de page
st.markdown("---")
st.markdown("👨‍💻 Réalisé par **Ange Désiré Boua** — M1 Big Data & IA — IUA")
st.caption("© 2025 - Mini projet académique (OpenCV + Streamlit)")
