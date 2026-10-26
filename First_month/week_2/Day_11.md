
## 1. What Is Probability?

**Probability** is a branch of mathematics that measures how likely an event is to happen.

Probability ranges from `0` to `1`.

- `0` means the event is impossible.
- `0.5` means the event has a 50% probability.
- `1` means the event is certain.

Probability can also be expressed as a percentage.

### Formula

For equally likely outcomes:

Probability = Number of favorable outcomes / Total number of possible outcomes

### Example 1: Tossing a Coin

A coin has two possible outcomes:

- Heads
- Tails

The probability of getting heads is:

P(Heads) = 1 / 2 = 0.5 = 50%

The probability of getting tails is also 50%.

### Example 2: Rolling a Die

A standard die has six possible outcomes:

`1, 2, 3, 4, 5, 6`

What is the probability of getting a 4?

P(4) = 1 / 6 ≈ 0.167 = 16.7%

What is the probability of getting an even number?

Even numbers are `2, 4, 6`.

P(Even) = 3 / 6 = 0.5 = 50%

### Important Probability Terms

**1. Experiment:** An action or process that produces an outcome.

Example: Tossing a coin.

**2. Outcome:** A possible result of an experiment.

Example: Heads.

**3. Sample Space:** The set of all possible outcomes.

Example: For a coin toss, the sample space is `{Heads, Tails}`.

**4. Event:** A particular outcome or group of outcomes.

Example: Getting an even number when rolling a die.

### Types of Probability

**1. Theoretical Probability**

Probability calculated using possible outcomes and mathematical reasoning.

Example: The probability of getting heads from a fair coin is 1/2.

**2. Experimental Probability**

Probability calculated from the results of actual experiments or observations.

Example: If a coin lands on heads 40 times in 100 tosses, the experimental probability is:

P(Heads) = 40 / 100 = 0.4 = 40%

**3. Conditional Probability**

Conditional probability measures the probability of an event occurring when another event is already known to have occurred.

Formula:

P(A | B) = P(A and B) / P(B)

Here, `P(A | B)` means the probability of event A given that event B has occurred, assuming P(B) is greater than zero.

### Uses of Probability in Machine Learning

- Predicting the likelihood of an event.
- Classifying emails as spam or not spam.
- Estimating the probability of a customer leaving a service.
- Understanding uncertainty in predictions.
- Supporting probabilistic models such as Naive Bayes.

**In simple words:** Probability helps us measure uncertainty and estimate how likely something is to happen.

---

## 2. What Is Correlation?

**Correlation** is a statistical measure that describes the direction and strength of the relationship between two variables.

For example, correlation can help us understand how house size is related to house price.

The Pearson correlation coefficient, usually represented by `r`, ranges from `-1` to `+1`.

### Types of Correlation

**1. Positive Correlation**

Positive correlation occurs when two variables tend to increase or decrease together.

Example: As house size increases, house price may also increase.

A correlation coefficient closer to `+1` indicates a stronger positive linear relationship.

**2. Negative Correlation**

Negative correlation occurs when one variable tends to increase as the other decreases.

Example: As the distance from a workplace increases, the attractiveness of a house to a particular commuter may decrease.

A correlation coefficient closer to `-1` indicates a stronger negative linear relationship.

**3. Zero or No Linear Correlation**

A correlation near zero indicates little or no linear relationship between two variables.

However, the variables may still have a nonlinear relationship.

### Understanding Correlation Values

| Correlation Coefficient (r) | Interpretation |
|---:|---|
| +1 | Perfect positive linear correlation |
| +0.8 | Strong positive linear correlation |
| +0.5 | Moderate positive linear correlation |
| 0 | No linear correlation |
| -0.5 | Moderate negative linear correlation |
| -0.8 | Strong negative linear correlation |
| -1 | Perfect negative linear correlation |

These strength descriptions are general guidelines. Interpretation depends on the data and context.

### Example

Consider the following data:

| House Size (sq. ft.) | House Price |
|---:|---:|
| 1000 | 3000000 |
| 1500 | 4000000 |
| 2000 | 5000000 |
| 2500 | 6000000 |

As house size increases, house price also increases.

This example shows a perfect positive linear relationship, so the Pearson correlation coefficient is `+1`.

### Correlation Formula

The Pearson correlation coefficient is calculated by dividing the covariance of two variables by the product of their standard deviations.

Where:
- `r` = Correlation coefficient.
- `x` and `y` = The two variables.
- `x̄` and `ȳ` = Their respective means.
- `n` = Number of observations.

### Correlation vs. Causation

**Correlation does not imply causation.**

This means that when two variables are related, it does not automatically mean one variable causes the other.

Example: Ice cream sales and swimming activity may both increase during hot weather. This does not mean that buying ice cream causes people to swim. Temperature may influence both.

### Uses of Correlation in Machine Learning

- Understanding relationships between features.
- Identifying highly correlated numerical variables.
- Exploring relationships between features and the target.
- Supporting feature selection.
- Performing exploratory data analysis.

**Important:** Correlation alone does not prove that a feature causes changes in the target or that it will improve model performance.

---

## 3. What Is a Train/Validation/Test Split?

A **train/validation/test split** is the process of dividing a dataset into separate parts for training a model, tuning it, and evaluating its final performance.

This helps us estimate how well a model performs on data it has not seen before.

### 1. Training Dataset

The training dataset is used to teach the model.

The model learns patterns and relationships between features and targets from this data.

Example: Teaching a model how house size, location, and bedrooms relate to house prices.

### 2. Validation Dataset

The validation dataset is used during model development to compare models, select hyperparameters, and make decisions about model design.

It helps us choose a suitable model without using the final test data.

### 3. Test Dataset

The test dataset is used to evaluate the final selected model.

It should remain separate from training and model selection so that the evaluation provides a more reliable estimate of performance on unseen data.

### Example of Dataset Splitting

Suppose a dataset contains 1,000 observations.

| Dataset | Percentage | Number of Observations | Purpose |
|---|---:|---:|---|
| Training | 70% | 700 | Train the model |
| Validation | 15% | 150 | Tune and compare models |
| Testing | 15% | 150 | Evaluate the final model |

This is one possible split. Other ratios, such as 80/10/10, can also be appropriate.

### Why Do We Split a Dataset?

- To train a model on one portion of the data.
- To tune the model without using test data.
- To detect overfitting.
- To evaluate performance on unseen observations.
- To estimate how well the model may generalize to new data.

### What Is Overfitting?

**Overfitting** occurs when a model learns the training data too closely, including noise or unimportant patterns, and performs poorly on unseen data.

A model may achieve excellent training performance but much worse validation performance.

A separate validation dataset helps identify this problem.

### What Is Underfitting?

**Underfitting** occurs when a model is too simple or insufficiently trained to learn the important patterns in the data.

It often performs poorly on both training and validation data.

### Important Rules for Data Splitting

1. Split the data before fitting preprocessing steps that learn from the data.
2. Fit scalers and imputers on the training data only, then apply them to validation and test data.
3. Do not use test results to repeatedly tune the model.
4. For classification, consider stratified splitting to preserve class proportions.
5. For time-series data, split chronologically rather than randomly when predicting future values.
6. For related observations, such as multiple records from the same customer, consider group-based splitting to prevent leakage.

### Train/Test Split Using Scikit-learn

```python
from sklearn.model_selection import train_test_split

# X contains features and y contains the target
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)
```

Here:
- `X` contains the input features.
- `y` contains the target variable.
- `test_size=0.2` reserves 20% of the data for testing.
- `random_state=42` makes the random split reproducible.

### Train/Validation/Test Split Using Scikit-learn

```python
from sklearn.model_selection import train_test_split

# First, separate the test dataset
X_temp, X_test, y_temp, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Then, split the remaining data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X_temp,
    y_temp,
    test_size=0.1875,
    random_state=42
)

print("Training:", X_train.shape)
print("Validation:", X_val.shape)
print("Testing:", X_test.shape)
```

This produces approximately:
- 65% training data.
- 15% validation data.
- 20% testing data.

The validation split is `0.1875` because it takes 18.75% of the remaining 80%, which equals 15% of the original dataset.

---

## 4. What Is Dataset Exploration?

**Dataset exploration**, also called Exploratory Data Analysis (EDA), is the process of examining and understanding a dataset before building a machine learning model.

The purpose is to understand the data structure, identify quality problems, discover patterns, and determine which preprocessing steps may be needed.

### Main Steps of Dataset Exploration

**1. Load the Dataset**

Read the data from a CSV, Excel file, or another supported source.

**2. Inspect the Dataset**

Check the first few rows, column names, number of rows, and number of columns.

**3. Check Data Types**

Determine whether columns contain integers, decimal values, text, dates, or categorical values.

**4. Check Missing Values**

Identify columns and rows containing missing values.

**5. Check Duplicate Records**

Determine whether the dataset contains duplicate observations.

**6. Calculate Statistical Summaries**

Use mean, median, minimum, maximum, standard deviation, and other summary statistics to understand numerical columns.

**7. Explore Categorical Variables**

Count the unique categories and examine their frequencies.

**8. Investigate Outliers**

Use summary statistics, histograms, box plots, and domain knowledge to identify unusual observations.

**9. Explore Relationships**

Use correlation matrices and scatter plots to investigate relationships between numerical variables.

**10. Decide on Preprocessing**

Based on the findings, decide whether to handle missing values, encode categories, scale numerical features, or investigate unusual records.

---

## 5. Dataset Exploration Using Pandas

Pandas is a Python library used for data manipulation and analysis.

### Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn
```

### Step 1: Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Step 2: Load the Dataset

```python
df = pd.read_csv("data.csv")
```

Replace `"data.csv"` with the path to your dataset.

### Step 3: Display the First Five Rows

```python
print(df.head())
```

This helps you understand how the dataset is organized.

### Step 4: Check the Dataset Shape

```python
print(df.shape)
```

Output example:

```text
(1000, 8)
```

This means the dataset contains 1,000 rows and 8 columns.

### Step 5: Display Column Names

```python
print(df.columns)
```

This displays the names of all columns.

### Step 6: Check Data Types

```python
print(df.dtypes)
```

This helps identify numerical, categorical, and other data types.

### Step 7: Get Dataset Information

```python
df.info()
```

This displays column names, non-null counts, data types, and memory usage.

### Step 8: Check Missing Values

```python
print(df.isnull().sum())
```

This displays the number of missing values in each column.

### Step 9: Check Duplicate Rows

```python
print("Duplicate rows:", df.duplicated().sum())
```

This counts rows that duplicate earlier rows across all columns.

Do not remove duplicates automatically without considering whether repeated records are valid.

### Step 10: Generate Statistical Summaries

```python
print(df.describe())
```

This displays statistics for numerical columns, including count, mean, standard deviation, minimum, quartiles, and maximum.

For categorical columns:

```python
print(df.describe(include="object"))
```

This summarizes object-type columns. Other categorical data types may need to be selected separately.

### Step 11: Check Unique Values

```python
for column in df.columns:
    print(f"\nColumn: {column}")
    print("Unique values:", df[column].nunique())
```

This helps identify columns with many unique values or only a few categories.

### Step 12: Check Correlation

```python
numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

print(correlation)
```

This calculates Pearson correlations between numerical columns by default.

### Step 13: Visualize Correlation Using a Heatmap

```python
plt.figure(figsize=(10, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.show()
```

A heatmap helps visualize the direction and strength of pairwise numerical correlations.

### Step 14: Plot a Histogram

```python
df["price"].hist(bins=30)

plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.show()
```

Replace `"price"` with a numerical column in your dataset.

A histogram helps you understand the distribution of values and identify potential skewness or unusual observations.

### Step 15: Plot a Scatter Plot

```python
plt.scatter(df["sqft_living"], df["price"])

plt.title("House Size vs House Price")
plt.xlabel("Living Area (sq. ft.)")
plt.ylabel("Price")

plt.show()
```

This plot helps you examine how living area relates to house price.

Replace the column names if your dataset uses different names.

---

## 6. Practical Task: Explore a Dataset

### Objective

Perform Exploratory Data Analysis on a dataset using Pandas, NumPy, Matplotlib, and Seaborn.

You can use your house price prediction dataset for this task.

### Task Requirements

**Part 1: Load and Inspect Data**

1. Load the dataset using Pandas.
2. Display the first 10 rows.
3. Display the last 5 rows.
4. Print the number of rows and columns.
5. Display all column names.
6. Check the data types of each column.

**Part 2: Data Quality Checks**

7. Count missing values in each column.
8. Count duplicate rows.
9. Count unique values in each column.
10. Identify numerical and categorical columns.

**Part 3: Statistical Analysis**

11. Calculate the mean of the house price column.
12. Calculate the median of the house price column.
13. Find the most frequent value of a selected column.
14. Calculate the standard deviation of numerical columns.
15. Display summary statistics using `describe()`.

**Part 4: Data Visualization**

16. Create a histogram of house prices.
17. Create a box plot of house prices.
18. Create a scatter plot of house size against house price.
19. Generate a correlation matrix for numerical columns.
20. Visualize the correlation matrix using a heatmap.

**Part 5: Write Your Observations**

Answer these questions after completing the analysis:

1. How many rows and columns are in the dataset?
2. Which columns contain missing values?
3. Are there any duplicate records?
4. Which numerical column has the highest standard deviation?
5. Is the house price distribution symmetric or skewed?
6. Are there any potential outliers in house prices?
7. Which numerical features have the strongest positive correlation with price?
8. Which features have negative correlation with price?
9. What preprocessing steps might be necessary before training a model?

Use the actual output of your dataset to answer these questions rather than assuming the results in advance.

---

