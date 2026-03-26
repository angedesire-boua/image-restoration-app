# 🖼️ Image Restoration App

Application web interactive de restauration d’images développée avec **Python**, **OpenCV** et **Streamlit**.  
Ce projet permet d’améliorer la qualité visuelle d’images dégradées grâce à plusieurs techniques classiques de traitement d’image.

---

## 📌 Aperçu du projet

Dans de nombreux domaines comme la **santé**, la **sécurité**, l’**archivage** ou les **médias**, la qualité d’une image est essentielle pour l’analyse et la prise de décision.  
Cependant, les images sont souvent altérées par du **bruit**, du **flou** ou une **faible netteté**.

Cette application propose une solution simple, interactive et intuitive pour :

- restaurer des images dégradées,
- comparer le rendu avant/après,
- tester plusieurs filtres de traitement,
- exporter l’image restaurée.

---

## 🚀 Fonctionnalités

- 📤 Upload d’image (**JPG / PNG**)
- 🎨 Conversion en **niveaux de gris**
- 🧼 Réduction du bruit avec :
  - **Filtre Gaussien**
  - **Filtre Médian**
  - **Filtre Bilatéral**
- ✨ Amélioration de la netteté avec :
  - **Filtre Laplacien**
- 🔍 Comparaison **Avant / Après**
- 💾 Téléchargement de l’image restaurée
- 🌐 Interface web interactive avec **Streamlit**

---

## 🛠️ Technologies utilisées

- **Python**
- **OpenCV**
- **NumPy**
- **Pillow**
- **Streamlit**

---

## 📂 Structure du projet

```bash
image-restoration-app/
│
├── app/                  # Code principal de l'application
├── docs/                 # Documentation ou rapport du projet
├── images/               # Images du projet / captures / exemples
├── README.md             # Documentation principale
└── requirements.txt      # Dépendances Python
