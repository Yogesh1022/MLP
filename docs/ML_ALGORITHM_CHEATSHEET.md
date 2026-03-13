# Machine Learning Algorithm Cheat Sheet (Simple + Practical)

This guide helps you quickly choose an algorithm by understanding:
- what your dataset looks like,
- what output you need,
- why one method is better than another,
- and common real-world use cases.

## 1) First choose problem type

1. Target column exists?
- Yes -> Supervised Learning
- No -> Unsupervised Learning

2. If supervised, what is target type?
- Number -> Regression
- Category/Class label -> Classification

3. Dataset size and shape
- Small + clean + interpretable needed -> linear/logistic/tree/LDA/Naive Bayes
- Medium + non-linear patterns -> Random Forest / Gradient Boosting / XGBoost / SVM / KNN
- Very large + many features / complex patterns -> MLP (neural net), boosting, or optimized methods

4. Need explainability vs accuracy
- Explainability first -> Linear models, Decision Tree, LDA, Naive Bayes
- Accuracy first -> XGBoost, Gradient Boosting, Random Forest, MLP

---

## 2) Supervised Algorithms

### Legend for data type fit
- Numeric: mostly continuous values
- Categorical: text/category values (usually encoded)
- Mixed: numeric + categorical
- Sparse: many zeros, high-dimensional vectors (text bag-of-words, one-hot)

| Algorithm | Shortcut trick (memory) | Best dataset type | Why use it | Typical use case |
|---|---|---|---|---|
| Linear Regression | Straight-line fit for numbers | Numeric, low/medium features, mostly linear relation | Fast, simple, interpretable baseline | House price prediction, sales forecasting |
| Multiple Linear Regression | Linear regression + many input columns | Numeric/mixed (encoded), low multicollinearity | Quantifies effect of each feature | Marketing mix impact, demand planning |
| Bayesian Regression | Linear regression with uncertainty/prior beliefs | Small/medium datasets, noisy data | Gives probability/uncertainty, robust for small data | Risk scoring with confidence intervals |
| Logistic Regression | Linear model for class probability | Binary classification, numeric/mixed (encoded) | Strong baseline, interpretable, fast | Churn yes/no, fraud flagging |
| Classification (general setup) | If target is category -> classification family | Any labeled class dataset | Converts data into class decisions | Spam vs non-spam, disease class |
| Decision Tree | Ask yes/no questions step by step | Mixed data, non-linear boundaries | Easy to explain, handles interactions | Credit approval rules, customer segmentation with labels |
| AdaBoost | Weak learners combined into a strong learner | Clean/medium tabular data, less noisy labels | Boosts weak models by focusing on mistakes | Fraud detection baseline boosting, risk classification |
| Random Forest | Many trees vote together | Mixed data, noisy data, non-linear | Better generalization than one tree, less overfitting | Default risk, quality inspection |
| Gradient Boosting | Trees learn from previous mistakes | Structured tabular data, medium size | Strong accuracy on tabular data | Claim prediction, churn, ranking |
| XGBoost | Optimized gradient boosting | Medium/large tabular, missing values possible | Top performance, regularization, fast | Kaggle-style tabular tasks, fraud/churn scoring |
| KNN | Similar points -> similar label/value | Numeric scaled data, low/medium dimensional | No training cost, simple intuition | Recommendation prototypes, pattern matching |
| SVM | Maximum margin separator | Medium dataset, high-dimensional/sparse data | Strong classifier with kernels for non-linear boundaries | Text classification, bioinformatics |
| Linear Discriminant Analysis (LDA) | Find projection that separates classes | Numeric features, roughly Gaussian classes | Fast and interpretable class separation | Face/biometric class separation, quality grading |
| Multi-class LDA | LDA extended to many classes | Numeric multiclass labels | Works well when class distributions are well behaved | Handwritten digit style structured data |
| Naive Bayes | Probability model with independence assumption | Text/sparse/high-dimensional categorical or counts | Very fast, great for text | Email spam, sentiment baseline |
| Perceptron | Single-layer linear neural classifier | Linearly separable classification | Very simple neural baseline | Intro binary classifiers, online learning |
| Multilayer Perceptron (MLP) | Neural net for complex non-linear mapping | Medium/large numeric data (scaled), complex patterns | Captures non-linearity and interactions | Demand pattern modeling, image/tabular hybrid patterns |
| Neuroevolution (supervised usage) | Use evolution to find neural architecture/weights | Complex search spaces where gradient methods struggle | Useful when architecture search is important | Auto-design neural policies/models |
| Particle Swarm Optimization (with supervised model tuning) | Swarm searches best hyperparameters | Any model needing parameter tuning | Gradient-free optimization of model settings | Hyperparameter tuning for SVM/NN |

### Quick supervised selection rules

- Start baseline:
  - Regression: Linear Regression
  - Classification: Logistic Regression or Decision Tree
- If baseline underfits (too simple):
  - Try Random Forest, Gradient Boosting, XGBoost, MLP
- If many text/sparse features:
  - Naive Bayes or linear/SVM models
- If dataset is small and interpretability is important:
  - Linear/Logistic/LDA/Decision Tree
- If you need best tabular performance quickly:
  - XGBoost or Gradient Boosting

### Other important supervised families (quick mention)

- Ridge/Lasso/ElasticNet: linear models with regularization when many correlated features exist.
- Extra Trees: randomized tree ensemble, often fast and strong.
- CatBoost/LightGBM: high-performance boosting libraries for tabular data.
- QDA: quadratic decision boundaries when LDA is too linear.
- Stacking/Blending: combine multiple supervised models for better performance.

---

## 3) Unsupervised Algorithms

| Algorithm | Shortcut trick (memory) | Best dataset type | Why use it | Typical use case |
|---|---|---|---|---|
| K-Means | Group by nearest center | Numeric scaled data, roughly spherical clusters | Fast, simple, scalable clustering | Customer grouping, document clustering |
| Partitioning Around Medoids (PAM) | Like K-means but uses real points (medoids) | Numeric with outliers, small/medium datasets | More robust to outliers than K-means | Store clustering with noisy transactions |
| DBSCAN | Dense regions become clusters, sparse = noise | Spatial/numeric with arbitrary cluster shapes | Finds irregular clusters + outliers automatically | GPS hotspot detection, anomaly clusters |
| Gaussian Mixture Model (GMM) | Soft clustering with probabilities | Numeric data where clusters overlap | Gives probability of belonging to each cluster | Market segment probability membership |
| PCA | Compress features into major directions | High-dimensional numeric data | Dimensionality reduction, denoising, visualization | Preprocessing before model, 2D visualization |
| Autoencoder | Neural compression-reconstruction | Large numeric/image/time-series data | Learns compact representation non-linearly | Anomaly detection, feature learning |
| Restricted Boltzmann Machine (RBM) | Generative feature extractor | Binary or normalized inputs, representation learning | Learns latent factors in unsupervised way | Recommender pretraining, feature extraction |
| Apriori | Frequent itemset mining by support/confidence | Transaction/basket data | Finds product co-occurrence rules | Market basket analysis |
| FP-Growth | Faster frequent pattern mining than Apriori | Large transaction datasets | Avoids heavy candidate generation | Retail bundle discovery |
| GAN (Generative Adversarial Network) | Generator vs discriminator game | Image/audio/text generation data | Generates realistic synthetic samples | Data augmentation, image generation |
| DCGAN | CNN-based GAN for images | Image datasets | Better image generation quality than basic GAN | Synthetic face/object generation |
| Genetic Algorithm (for unsupervised optimization) | Evolution finds best clustering/feature subset | Any data with hard optimization objective | Global search without gradients | Feature subset selection, clustering objective optimization |

### Other important unsupervised families (quick mention)

- Hierarchical Clustering: tree-like cluster relationship discovery.
- t-SNE/UMAP: non-linear dimensionality reduction for visualization.
- Isolation Forest/One-Class SVM: anomaly detection without labels.
- NMF: parts-based matrix decomposition, useful in topic modeling.
- Spectral Clustering: handles non-convex clusters via graph structure.

### Notes on optimization methods

- Genetic Algorithm, Particle Swarm Optimization, and Neuroevolution are optimization frameworks.
- They are often used to tune or search models rather than being direct predictors by themselves.

### Quick unsupervised selection rules

- Need clusters, unknown groups:
  - Start with K-Means (fast baseline)
  - If irregular shapes/outliers: DBSCAN
  - If overlapping clusters and probability needed: GMM
- Need fewer features/visualization:
  - PCA (simple, fast)
  - Autoencoder (complex non-linear structures)
- Need association rules from basket data:
  - Apriori / FP-Growth
- Need synthetic data generation:
  - GAN / DCGAN

---

## 4) Fast dataset-to-algorithm mapping

| Dataset pattern | Good first choice | Strong next choice |
|---|---|---|
| Numeric target, linear trend | Linear Regression | Gradient Boosting / XGBoost |
| Numeric target, strong non-linearity | Random Forest Regressor | XGBoost Regressor / MLP |
| Binary class, explainability needed | Logistic Regression | Decision Tree |
| Binary/multiclass, best tabular accuracy | Random Forest | XGBoost / Gradient Boosting |
| Text/sparse features | Naive Bayes | Linear SVM |
| Many classes with numeric features | Multi-class LDA | Random Forest / XGBoost |
| Unknown customer groups | K-Means | GMM / DBSCAN |
| Outlier detection in clusters | DBSCAN | Autoencoder (reconstruction error) |
| Basket transactions | Apriori | FP-Growth |
| High-dimensional compression | PCA | Autoencoder |
| Image generation | DCGAN | Advanced GAN variants |

---

## 5) One-line choosing formula

Use this simple formula:

- Task type + Data shape + Interpretability need + Scale/speed need + Accuracy target

Example:
- If data is tabular, mixed features, supervised classification, and you need high accuracy quickly -> start with XGBoost.
- If data is small and you must explain every decision -> start with Logistic Regression or Decision Tree.
- If no labels and you want customer groups -> start with K-Means, then validate with DBSCAN/GMM.

---

## 6) Common mistakes to avoid

- Using unscaled features with KNN/SVM/K-Means.
- Using only accuracy for imbalanced classes (use precision, recall, F1, ROC-AUC).
- Choosing complex deep models for tiny tabular datasets.
- Ignoring baseline models before moving to advanced models.
- Not validating with cross-validation and holdout test set.

---

## 7) Practical workflow (cheat process)

1. Define target type (regression/classification/none).
2. Start with simplest baseline model.
3. Check error metrics and failure patterns.
4. Upgrade to stronger model family if needed.
5. Compare with cross-validation.
6. Pick model balancing performance + explainability + deployment cost.

This process helps you predict the right algorithm from dataset properties in simple words and with less trial-and-error.
