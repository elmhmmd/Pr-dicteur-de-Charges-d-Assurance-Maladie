# Prédicteur de Charges d'Assurance Maladie

## 📋 Présentation

Ce projet vise à développer un modèle de régression performant pour prédire les charges à payer à l'assurance maladie. L'objectif est de fournir une solution rapide, fiable et accessible pour aider les utilisateurs à anticiper leurs dépenses de santé.

## **Objectif métier** : Prédire précisément les charges médicales individuelles à partir de dossiers assurés comprenant :
  - Âge (`Age`)
  - Sexe (`Sex`)
  - Indice de masse corporelle (`BMI`)
  - Nombre d’enfants à charge (`Children`)
  - Habitude tabagique (`Smoker`)
  - Région géographique (`Region`)

## 🧑‍🔬 Pipeline & Fonctionnalités

### 1. Analyse et Préparation des Données
- Import et exploration (`pandas`, `matplotlib`, `seaborn`)
- Analyse descriptive et détection des valeurs manquantes/doublons
- Visualisation des distributions et corrélations
- Prétraitement : imputation, suppression des doublons, gestion des outliers, encodage des variables catégoriques, normalisation/standardisation

### 2. Entraînement des Modèles de Régression
- Implémentation et évaluation de plusieurs modèles : 
  - `LinearRegression`
  - `RandomForestRegressor`
  - `XGBRegressor`
  - `SVR`
- Pipelines intégrant preprocessing + modèle
- Métriques : RMSE, MAE, R²

### 3. Tuning des Hyperparamètres
- Sélection des meilleurs modèles
- Recherche GridSearchCV / RandomizedSearchCV (validation croisée 5 folds)
- Amélioration des performances

### 4. Évaluation et Comparaison
- Visualisations comparatives : graphiques de résidus, scatter plots
- Tableau récapitulatif des performances
- Sélection du modèle final selon robustesse et généralisation

### 5. Test, Export et Déploiement
- Export du modèle (`joblib`/`pickle`)
- Interface utilisateur simple pour tester une prédiction à partir de données saisies

### 6. Documentation et Reproductibilité
- Code commenté et étapes détaillées dans chaque notebook
- Instructions claires d’exécution

## 🚀 Comment exécuter le projet

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/elmhmmd/Pr-dicteur-de-Charges-d-Assurance-Maladie.git
   cd Pr-dicteur-de-Charges-d-Assurance-Maladie
   ```
2. **Installer les dépendances**
   ```bash
   pip install numpy pandas seaborn scikit-learn xgboost matplotlib
   ```
3. **Lancer le notebook Jupyter pour l'exploration et l'entraînement du modèle**
    ```bash
   jupyter notebook Assurance.ipynb 
   ```
4. **Lancer l'interface Streamlit**
    ```bash
   streamlit run Interface.py
   ```
   
   
