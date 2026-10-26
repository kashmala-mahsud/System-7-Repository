# Linear and Multiple Linear Regression, Classification vs. Regression, and Scikit-learn Workflow

## 1. Linear Regression

### Definition

Linear Regression is a supervised machine learning algorithm used to predict a continuous numerical value by finding a linear relationship between input features and the target variable.

Examples:
- Predicting house prices
- Predicting a student's marks
- Predicting monthly sales
- Predicting salary based on experience

### Formula

The equation of simple linear regression is:

\[
\hat{y} = b_0 + b_1x
\]

Where:
- `ŷ` = Predicted value
- `x` = Input feature
- `b₀` = Intercept
- `b₁` = Slope or coefficient

### Example

Suppose we want to predict a house price based on its size.

| House Size (sq. ft.) | Price |
|---:|---:|
| 1000 | 200000 |
| 1500 | 300000 |
| 2000 | 400000 |

The model learns the relationship between house size and price. If the relationship continues, it can predict the price of a house with a size of 2500 square feet.

### Python Example

```python
import numpy as np
from sklearn.linear_model import LinearRegression

# Input feature
X = np.array([[1000], [1500], [2000]])

# Target variable
y = np.array([200000, 300000, 400000])

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict house price
prediction = model.predict([[2500]])

print("Predicted Price:", prediction[0])
```

Expected prediction:

```text
Predicted Price: 500000.0
```

### Advantages
- Simple and easy to understand.
- Fast to train.
- Easy to interpret.
- Works well when the relationship is approximately linear.

### Limitations
- May perform poorly when relationships are nonlinear.
- Sensitive to outliers.
- Can underfit complex datasets.

---

## 2. Multiple Linear Regression

### Definition

Multiple Linear Regression is a supervised machine learning algorithm that predicts a continuous numerical value using two or more input features.

Simple Linear Regression uses one input feature, while Multiple Linear Regression uses multiple input features.

### Formula

\[
\hat{y} = b_0 + b_1x_1 + b_2x_2 + \cdots + b_nx_n
\]

Where:
- `ŷ` = Predicted value
- `b₀` = Intercept
- `x₁, x₂, ..., xₙ` = Input features
- `b₁, b₂, ..., bₙ` = Feature coefficients

### Example

To predict a house price, we might use:
- House size
- Number of bedrooms
- Number of bathrooms
- Number of floors

The model learns how these features relate to the house price.

### Python Example

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

# Create dataset
data = {
    "size": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 5],
    "bathrooms": [1, 2, 2, 3, 4],
    "price": [200000, 300000, 350000, 450000, 550000]
}

df = pd.DataFrame(data)

# Select input features
X = df[["size", "bedrooms", "bathrooms"]]

# Select target variable
y = df["price"]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict the price of a new house
prediction = model.predict([[2200, 3, 2]])

print("Predicted Price:", prediction[0])
```

The prediction is a numerical value estimated from the relationships learned during training.

**Note:** Scikit-learn may display a warning because the prediction input is a list rather than a DataFrame with feature names. To avoid it, use:

```python
new_house = pd.DataFrame({
    "size": [2200],
    "bedrooms": [3],
    "bathrooms": [2]
})

prediction = model.predict(new_house)
print("Predicted Price:", prediction[0])
```

### Difference Between Simple and Multiple Linear Regression

| Simple Linear Regression | Multiple Linear Regression |
|---|---|
| Uses one input feature. | Uses two or more input features. |
| Has one feature coefficient and an intercept. | Has multiple feature coefficients and an intercept. |
| Example: Price based on size. | Example: Price based on size, bedrooms, and bathrooms. |

---

## 3. Classification vs. Regression

Both are supervised machine learning tasks. The main difference is the type of output they predict.

### Regression

Regression predicts a continuous numerical value.

Examples:
- House price: 250000
- Temperature: 32.5°C
- Salary: 80000
- Sales: 12500 units

Common algorithms:
- Linear Regression
- Multiple Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Common evaluation metrics:
- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

### Classification

Classification predicts a category or class label.

Examples:
- Email: Spam or Not Spam
- Disease prediction: Positive or Negative
- Image: Cat, Dog, or Bird
- Customer: Will Buy or Will Not Buy

Common algorithms:
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)

Common evaluation metrics:
- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Comparison Table

| Feature | Regression | Classification |
|---|---|---|
| Output | Numerical value | Category or class |
| Example | Predict house price | Predict spam email |
| Target | Continuous | Categorical |
| Common metrics | MAE, RMSE, R² | Accuracy, Precision, Recall, F1 |
| Example algorithm | Linear Regression | Logistic Regression |

**Important:** Despite its name, Logistic Regression is generally used for classification, not ordinary regression.

---

## 4. Scikit-learn Workflow

### Definition

Scikit-learn is a Python machine learning library that provides tools for data preprocessing, model training, prediction, and evaluation.

It supports many machine learning algorithms, including Linear Regression, Logistic Regression, Decision Trees, Random Forests, and KNN.

### Standard Machine Learning Workflow

1. Import libraries.
2. Load the dataset.
3. Explore and clean the data.
4. Select input features (`X`) and target (`y`).
5. Split the data into training and testing sets.
6. Create a model.
7. Train the model using `fit()`.
8. Make predictions using `predict()`.
9. Evaluate the model.
10. Improve the model if needed.

### Important Scikit-learn Functions

| Function | Purpose |
|---|---|
| `train_test_split()` | Splits data into training and testing sets. |
| `LinearRegression()` | Creates a linear regression model. |
| `fit()` | Trains the model. |
| `predict()` | Generates predictions. |
| `mean_absolute_error()` | Calculates MAE. |
| `mean_squared_error()` | Calculates MSE. |
| `r2_score()` | Calculates the R² score. |

### Complete Example: House Price Prediction

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Load dataset
df = pd.read_csv("house_prices.csv")

# Select input features
X = df[["sqft_living", "bedrooms", "bathrooms"]]

# Select target variable
y = df["price"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
```

**Note:** Replace `house_prices.csv` with your actual dataset filename. The column names must match the columns in your dataset.

### Understanding the Code

**1. Selecting features and target**

```python
X = df[["sqft_living", "bedrooms", "bathrooms"]]
y = df["price"]
```

- `X` contains the input features used to make predictions.
- `y` contains the actual values the model learns to predict.

**2. Splitting the dataset**

```python
train_test_split(X, y, test_size=0.2, random_state=42)
```

- 80% of the data is used for training.
- 20% is used for testing.
- `random_state=42` makes the split reproducible.

**3. Training the model**

```python
model.fit(X_train, y_train)
```

The model learns the relationship between the input features and house prices.

**4. Making predictions**

```python
y_pred = model.predict(X_test)
```

The trained model predicts prices for the test data.

**5. Evaluating the model**

The evaluation metrics compare predicted prices with actual prices to measure model performance.

---

## 5. Regression Evaluation Metrics

### MAE (Mean Absolute Error)

MAE measures the average absolute difference between actual and predicted values.

A lower MAE generally indicates better predictions.

### MSE (Mean Squared Error)

MSE calculates the average of squared prediction errors. Large errors receive greater penalties because the errors are squared.

A lower MSE generally indicates better predictions.

### RMSE (Root Mean Squared Error)

RMSE is the square root of MSE. It is expressed in the same units as the target variable.

For house prices, RMSE is expressed in the currency used by the dataset.

### R² Score

R² measures how well the model explains variation in the target variable.

- `1.0`: Perfect predictions.
- `0.0`: No improvement over predicting the target mean, under the usual evaluation setup.
- Negative value: Worse than predicting the target mean on the evaluation data.

A higher R² is generally better, but metrics should be interpreted in context.

---


