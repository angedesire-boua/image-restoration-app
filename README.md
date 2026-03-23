# Image Restoration App

Application de restauration d’images basée sur des techniques classiques de traitement d’image, développée avec Python, OpenCV et Streamlit.

---

## 1. Présentation

Ce projet propose une solution interactive permettant d’améliorer la qualité d’images dégradées (floues ou bruitées) à travers un pipeline de traitement simple et efficace.

Dans un contexte où les images sont omniprésentes (santé, sécurité, archivage), leur qualité influence directement leur exploitabilité. Cette application vise à démontrer comment des méthodes accessibles peuvent restaurer la lisibilité d’images altérées.

---

## 2. Objectifs

- Implémenter un pipeline complet de traitement d’image
- Appliquer des techniques de débruitage et d’amélioration de netteté
- Proposer une interface interactive simple (Streamlit)
- Visualiser l’impact des traitements (avant / après)
- Illustrer des cas d’usage concrets du traitement d’image

---

## 3. Fonctionnalités

- Import d’image (jpg, png)
- Conversion en niveaux de gris
- Réduction du bruit avec :
  - Filtre Gaussien
  - Filtre Médian
  - Filtre Bilatéral
- Amélioration de la netteté (filtre Laplacien)
- Affichage comparatif (image originale vs restaurée)
- Téléchargement de l’image traitée

---

## 4. Pipeline de traitement

1. Chargement de l’image
2. Conversion en niveaux de gris
3. Application d’un filtre de débruitage
4. Renforcement des contours (Laplacien)
5. Affichage du résultat
6. Export de l’image restaurée

---

## 5. Stack technique

- **Python** : langage principal
- **OpenCV** : traitement d’image
- **Streamlit** : interface utilisateur
- **NumPy** : manipulation de données
- **Pillow (PIL)** : gestion des images
