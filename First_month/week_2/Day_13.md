
## 1. Logistic Regression

### Definition

Logistic Regression is a supervised machine learning algorithm mainly used for classification. It predicts the probability that an observation belongs to a particular class.

Despite its name, Logistic Regression is generally used for classification rather than predicting continuous numerical values.

### Examples
- Predict whether an email is spam or not spam.
- Predict whether a customer will buy a product.
- Predict whether a patient has a disease.
- Predict whether a loan applicant will default.

### How It Works

Logistic Regression calculates a probability between 0 and 1 using the logistic (sigmoid) function. A threshold is then used to assign a class.

For example:
- Probability = 0.85: predict class 1.
- Probability = 0.20: predict class 0.

With the default threshold of 0.5, probabilities of 0.5 or higher are classified as class 1.

### Formula

\[
P(Y=1)=\frac{1}{1+e^{-z}}
\]

Where:

\[
z=b_0+b_1x_1+\cdots+b_nx_n
\]

- `P(Y=1)` = Probability of class 1.
- `e` = Mathematical constant.
- `b₀` = Intercept.
- `b₁, ..., bₙ` = Model coefficients.
- `x₁, ..., xₙ` = Input features.

### Python Example

```python
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features using training data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create and train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### Advantages
- Simple and relatively fast.
- Provides class probabilities.
- Coefficients can help explain feature relationships.
- Works well when the decision boundary is approximately linear in the model's transformed feature space.

### Limitations
- May not perform well with complex nonlinear decision boundaries without feature engineering.
- Can be affected by highly correlated features.
- Feature scaling is often helpful, especially when regularization is used.

---

## 2. K-Nearest Neighbors (KNN)

### Definition

K-Nearest Neighbors is a supervised machine learning algorithm used for classification and regression. It makes predictions by looking at the `K` closest data points to a new observation.

### How It Works

Suppose we want to classify a new data point.

1. Choose a value for `K`.
2. Calculate the distance between the new point and the training points.
3. Find the `K` nearest neighbors.
4. For classification, choose the majority class among the neighbors.
5. For regression, calculate an average of their target values.

### Example

Suppose `K = 3`, and the three nearest neighbors have these labels:

- Cat
- Cat
- Dog

KNN predicts **Cat** because it is the majority class.

### Distance Formula

Euclidean distance between two points is:

\[
d=\sqrt{\sum_{i=1}^{n}(x_i-y_i)^2}
\]

Where:
- `d` = Distance between two points.
- `xᵢ` and `yᵢ` = Feature values.
- `n` = Number of features.

### Python Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=5)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
```

### What Is K?

`K` is the number of neighbors considered when making a prediction.

- Small K: Can be sensitive to noise and may overfit.
- Large K: Creates smoother decisions but may underfit.

The best value of K depends on the dataset and can be selected using validation or cross-validation.

### Advantages
- Easy to understand and implement.
- Can model nonlinear decision boundaries.
- Requires little training time because it mainly stores the training data.

### Limitations
- Prediction can be slow for large datasets.
- Sensitive to feature scales.
- Can perform poorly with many irrelevant features or very high-dimensional data.
- Requires choosing a suitable K value.

---

## 3. Decision Trees

### Definition

A Decision Tree is a supervised machine learning algorithm used for classification and regression. It makes predictions by splitting data into smaller groups based on feature values.

### How It Works

A decision tree consists of:

- **Root node:** The first decision or split.
- **Internal nodes:** Additional decisions based on features.
- **Branches:** The outcomes of decisions.
- **Leaf nodes:** The final prediction.

### Example

Suppose we want to predict whether a person will buy a product.

```text
Income > 50000?
    |
    |-- Yes --> Will the person visit the website?
    |               |
    |               |-- Yes --> Buy
    |               |-- No  --> Not Buy
    |
    |-- No  --> Not Buy
```

This is an illustrative decision tree. A trained tree learns its actual splits from data.

### How Does a Tree Choose Splits?

For classification, common criteria include:

- **Gini impurity:** Measures how mixed the classes are in a node.
- **Entropy:** Measures uncertainty in a node.
- **Information gain:** Measures the reduction in entropy after a split.

A good split separates the classes more effectively.

For regression, a decision tree commonly chooses splits that reduce squared prediction error within the resulting groups.

### Python Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
```

### Important Parameters

- `max_depth`: Maximum depth of the tree.
- `min_samples_split`: Minimum number of samples required to split a node.
- `min_samples_leaf`: Minimum number of samples allowed in a leaf.
- `criterion`: The measure used to evaluate splits.

### Advantages
- Easy to visualize and interpret.
- Handles nonlinear relationships.
- Usually does not require feature scaling.
- Can be used for classification and regression.

### Limitations
- A deep tree can overfit training data.
- Small changes in the data can produce a different tree.
- A single tree may be less accurate than an ensemble of trees.

---

## 4. Random Forests

### Definition

Random Forest is a supervised machine learning algorithm that combines multiple decision trees to make predictions.

It is an ensemble learning method because it combines the predictions of several models.

### How It Works

1. Randomly sample training data to build different trees.
2. Train each tree using a random subset of features at each split.
3. Obtain predictions from all the trees.
4. Combine the predictions.

For classification, the forest typically uses majority voting.

For regression, it typically averages the predictions from its trees.

### Example

Suppose a random forest contains five decision trees:

| Tree | Prediction |
|---|---|
| Tree 1 | Spam |
| Tree 2 | Spam |
| Tree 3 | Not Spam |
| Tree 4 | Spam |
| Tree 5 | Not Spam |

The final prediction is **Spam**, because three out of five trees predict Spam.

### Python Example

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create random forest
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=5,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

### Important Parameters

- `n_estimators`: Number of trees in the forest.
- `max_depth`: Maximum depth of each tree.
- `min_samples_split`: Minimum samples required to split a node.
- `min_samples_leaf`: Minimum samples required in a leaf.
- `max_features`: Number or proportion of features considered at each split.

### Advantages
- Often performs well on structured, tabular datasets.
- Usually less prone to overfitting than a single deep decision tree.
- Handles nonlinear relationships.
- Can estimate feature importance.

### Limitations
- Requires more memory than a single tree.
- Can take longer to train.
- Is less interpretable than an individual decision tree.
- Feature importance can be misleading when features are correlated or have different measurement properties.

---

## 5. Comparison of the Four Algorithms

| Feature | Logistic Regression | KNN | Decision Tree | Random Forest |
|---|---|---|---|---|
| Main use | Classification | Classification and regression | Classification and regression | Classification and regression |
| Basic idea | Estimates class probabilities | Uses nearby data points | Learns decision rules | Combines many trees |
| Feature scaling | Often helpful | Usually important | Usually unnecessary | Usually unnecessary |
| Interpretability | Relatively high | Easy concept, predictions can be hard to explain | High for small trees | Lower than one tree |
| Training speed | Usually fast | Very fast to fit | Usually fast | Usually slower than one tree |
| Prediction speed | Usually fast | Can be slow on large datasets | Usually fast | Depends on forest size |

---

## 6. Model Evaluation for Classification

### Accuracy

Accuracy measures the proportion of predictions that are correct.

\[
Accuracy=\frac{\text{Correct Predictions}}{\text{Total Predictions}}
\]

Accuracy can be misleading when one class is much more common than another.

### Precision

Precision measures how many predicted positive cases are actually positive.

\[
Precision=\frac{TP}{TP+FP}
\]

### Recall

Recall measures how many actual positive cases the model correctly identifies.

\[
Recall=\frac{TP}{TP+FN}
\]

### F1 Score

F1 Score combines precision and recall using their harmonic mean.

\[
F1=2\times\frac{Precision\times Recall}{Precision+Recall}
\]

Where:

- `TP` = True Positives
- `FP` = False Positives
- `TN` = True Negatives
- `FN` = False Negatives

In Scikit-learn, use `accuracy_score()` and `classification_report()` to calculate common classification metrics.

---

