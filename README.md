# Image Restoration App

Application de restauration d’images basée sur des techniques de traitement d’image numérique, développée avec Python, OpenCV et Streamlit.

---

## 1. Contexte

Dans de nombreux domaines (santé, sécurité, archivage, médias), la qualité des images est essentielle pour l’analyse et la prise de décision. Pourtant, les images sont souvent dégradées (flou, bruit, faible contraste) en raison de conditions de capture imparfaites.

Ce projet propose une solution simple et interactive permettant d’améliorer la lisibilité d’images dégradées à l’aide de techniques classiques de vision par ordinateur.

---

## 2. Objectif

Concevoir une application web permettant de :

- Restaurer des images floues ou bruitées  
- Appliquer des filtres de traitement d’image  
- Visualiser les résultats en temps réel  
- Comparer les images avant et après traitement  
- Télécharger l’image restaurée  

---

## 3. Fonctionnalités

- Upload d’image (JPG, PNG)  
- Conversion en niveaux de gris  
- Réduction du bruit :
  - Filtre Gaussien  
  - Filtre Médian  
  - Filtre Bilatéral  
- Amélioration de la netteté :
  - Filtre Laplacien  
- Affichage comparatif (avant / après)  
- Export de l’image restaurée  

---

## 4. Pipeline de traitement

1. Chargement de l’image  
2. Conversion en niveaux de gris  
3. Application d’un filtre de débruitage  
4. Amélioration de la netteté (accentuation des contours)  
5. Affichage du résultat  
6. Téléchargement de l’image finale  

---

## 5. Technologies utilisées

- **Python** : langage principal  
- **OpenCV** : traitement d’image  
- **Streamlit** : interface web interactive  
- **NumPy** : calcul numérique  
- **Pillow (PIL)** : manipulation d’images  

---

## 6. Installation

```bash
git clone https://github.com/angedesire-boua/image-restoration-app.git
cd image-restoration-app
pip install -r requirements.txt
