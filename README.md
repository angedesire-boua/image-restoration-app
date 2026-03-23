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

Le processus de traitement suit les étapes suivantes :

1. Chargement de l’image  
2. Conversion en niveaux de gris  
3. Application d’un filtre de débruitage  
4. Amélioration de la netteté (accentuation des contours)  
5. Affichage du résultat  
6. Téléchargement de l’image finale  

---


---

## 6. Technologies utilisées

- **Python** : langage principal  
- **OpenCV** : traitement d’image  
- **Streamlit** : interface web interactive  
- **NumPy** : calcul numérique  
- **Pillow (PIL)** : manipulation d’images  

---

## 7. Installation

Cloner le dépôt :

```bash
git clone https://github.com/angedesire-boua/image-restoration-app.git
cd image-restoration-app

---

## 9. Résultats

L’application permet :

- Une réduction visible du bruit
- Une amélioration de la netteté
- Une meilleure lisibilité des images
- Une comparaison directe entre image originale et image traitée

---

## 10. Cas d’usage
- Santé : amélioration d’images médicales (radiographie, IRM)
- Sécurité : clarification d’images de vidéosurveillance
- Archivage : restauration de documents anciens
- Usage quotidien : amélioration de photos prises avec des appareils de faible qualité

---

## 11. Limites
Traitement uniquement en niveaux de gris
Paramètres des filtres non ajustables
Méthodes classiques (pas d’apprentissage profond)
Résultats limités sur des images fortement dégradées

---

## 12. Perspectives d’amélioration
Intégration de modèles de Deep Learning (GAN, Autoencoders)
Support du traitement en couleur
Ajout de paramètres ajustables (intensité des filtres)
Détection automatique des zones dégradées
Déploiement en ligne (cloud)
Traitement par lot

---

##13. Rapport

Le rapport complet du projet est disponible dans :

docs/report.pdf

---

##14. Auteur

Ange Désiré Boua
Master Big Data & Intelligence Artificielle
Institut Universitaire d’Abidjan (IUA)

---

##15. Positionnement

Ce projet constitue une implémentation complète d’un pipeline de traitement d’image, allant de l’acquisition à la restitution, avec une approche orientée application.

Il sert de base pour évoluer vers des systèmes plus avancés en vision par ordinateur et en intelligence artificielle.
