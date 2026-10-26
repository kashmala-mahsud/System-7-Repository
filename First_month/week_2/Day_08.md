## 1. What is Artificial Intelligence (AI)?

Artificial Intelligence (AI) is a branch of computer science that focuses on creating machines and computer systems that can perform tasks that typically require human intelligence, such as learning, reasoning, problem-solving, and understanding language.

**Examples:**
- ChatGPT answering questions.
- Virtual assistants understanding voice commands.
- Self-driving cars identifying roads and pedestrians.
- Recommendation systems suggesting movies and products.

**In simple words:** AI enables machines to perform tasks that normally require human intelligence.

## 2. What is Machine Learning (ML)?

Machine Learning (ML) is a branch of Artificial Intelligence that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed for every situation.

**Examples:**
- Predicting house prices.
- Detecting spam emails.
- Predicting customer behavior.
- Recommending products.

**In simple words:** Machine Learning allows computers to learn from data and make predictions or decisions.

## 3. What is Deep Learning (DL)?

Deep Learning (DL) is a subfield of Machine Learning that uses artificial neural networks with multiple layers to learn complex patterns from large amounts of data.

It is commonly used for image recognition, speech recognition, natural language processing, and other complex tasks.

**Examples:**
- Facial recognition.
- Speech recognition.
- Image classification.
- Large Language Models (LLMs).

**In simple words:** Deep Learning uses multi-layered neural networks to learn complex patterns from data.

## 4. Difference Between AI, ML, and Deep Learning

| Feature | AI | ML | Deep Learning |
|---|---|---|---|
| Definition | Enables machines to perform intelligent tasks. | Enables machines to learn from data. | Uses multi-layered neural networks to learn complex patterns. |
| Scope | Broadest field. | A subfield of AI. | A subfield of ML. |
| Examples | AI assistants, rule-based systems. | House price prediction, spam detection. | Image recognition, speech recognition, LLMs. |

**Relationship:**

AI → Machine Learning → Deep Learning

Deep Learning is a subset of Machine Learning, and Machine Learning is a subset of Artificial Intelligence.

## 5. What is Supervised Learning?

Supervised Learning is a type of Machine Learning in which a model learns from labeled data. The data contains input features and their corresponding correct answers.

The model learns patterns from the training data and uses them to make predictions on new data.

**Examples:**
- Predicting house prices.
- Classifying emails as spam or not spam.
- Predicting students' exam scores.
- Detecting objects in images.

### Types of Supervised Learning

**1. Regression**

Regression is used to predict continuous numerical values.

Examples:
- Predicting house prices.
- Predicting temperature.
- Estimating salaries.

**2. Classification**

Classification is used to predict categories or classes.

Examples:
- Classifying emails as spam or not spam.
- Predicting whether a customer will leave or stay.
- Classifying images as cats or dogs.

**In simple words:** Supervised Learning learns from data that already contains the correct answers.

## 6. What is Unsupervised Learning?

Unsupervised Learning is a type of Machine Learning in which a model learns patterns and relationships from unlabeled data.

The data does not contain predefined correct answers. The model discovers useful patterns or groups in the data.

**Examples:**
- Grouping customers based on purchasing behavior.
- Grouping similar documents.
- Discovering patterns in customer data.
- Identifying unusual data points.

### Common Techniques

**1. Clustering**

Clustering groups similar data points together.

Example: Grouping customers according to their spending habits.

**2. Dimensionality Reduction**

Dimensionality reduction reduces the number of features while preserving as much useful information as possible.

Example: Reducing hundreds of features to a smaller set for visualization.

**In simple words:** Unsupervised Learning discovers hidden patterns or groups in data without predefined labels.

## 7. What is Reinforcement Learning?

Reinforcement Learning (RL) is a type of Machine Learning in which an agent learns to make decisions by interacting with an environment and receiving rewards or penalties based on its actions.

The goal is to learn a strategy that maximizes the total reward over time.

### Main Components of Reinforcement Learning

1. **Agent:** The learner or decision-maker.
2. **Environment:** The world in which the agent operates.
3. **Action:** A decision or move made by the agent.
4. **Reward:** Feedback indicating how beneficial an action was.
5. **State:** The current situation of the environment.
6. **Policy:** The strategy used by the agent to choose actions.

**Examples:**
- Training an agent to play a video game.
- Teaching a robot to navigate an environment.
- Training systems to make decisions through repeated interactions.

**In simple words:** Reinforcement Learning allows an agent to learn through actions and feedback from its environment.

## 8. Difference Between Supervised, Unsupervised, and Reinforcement Learning

| Feature | Supervised Learning | Unsupervised Learning | Reinforcement Learning |
|---|---|---|---|
| Data | Labeled data | Unlabeled data | Experience from interactions |
| Goal | Predict outputs | Discover patterns | Maximize rewards |
| Feedback | Correct answers | No predefined target labels | Rewards or penalties |
| Common tasks | Regression and classification | Clustering and dimensionality reduction | Sequential decision-making |
| Example | House price prediction | Customer segmentation | Training a game-playing agent |

## 9. What is a Dataset?

A dataset is a collection of related data organized for analysis, processing, or training machine learning models.

A dataset can contain numbers, text, images, audio, or other types of information.

**Examples:**
- House price dataset.
- Customer information dataset.
- Images of cats and dogs.
- Emails labeled as spam or not spam.

Datasets are commonly stored in CSV, Excel, JSON, or database tables.

**In simple words:** A dataset is a collection of data used for analysis or model training.

## 10. What are the Main Terms Used in a Dataset?

Consider the following house price dataset:

| Size (sq. ft.) | Bedrooms | Age (years) | Price |
|---:|---:|---:|---:|
| 1000 | 2 | 10 | 5000000 |
| 1500 | 3 | 5 | 7000000 |
| 2000 | 4 | 2 | 9000000 |
| 1200 | 2 | 8 | 5500000 |

### 10.1 Data

Data consists of individual facts, values, or observations.

Example: `1500`, `3`, and `7000000` are data values in the house price dataset.

### 10.2 Dataset

A dataset is the complete collection of related data.

Example: The entire house price table is a dataset.

### 10.3 Row

A row represents one record or observation in a dataset.

Example: The first row describes a house with a size of 1000 square feet, two bedrooms, an age of 10 years, and a price of 5000000.

### 10.4 Column

A column represents a particular attribute or variable.

Examples:
- Size
- Bedrooms
- Age
- Price

### 10.5 Feature

A feature is an input variable used by a machine learning model to make predictions.

Examples:
- House size.
- Number of bedrooms.
- House age.

**In simple words:** Features are the input information used by a model to make predictions.

### 10.6 Target Variable

The target variable is the value that a supervised learning model is trained to predict.

Example: In house price prediction, `Price` is the target variable.

### 10.7 Label

A label is the correct answer associated with an example in a labeled dataset, especially in classification tasks.

Example:

| Email | Label |
|---|---|
| You won a prize! | Spam |
| Meeting at 10 AM | Not Spam |

Here, `Spam` and `Not Spam` are labels.

**Note:** In regression, the target is a numerical value. In classification, the target is a category.

### 10.8 Observation

An observation is one individual example or record in a dataset.

Example: One house's complete information represents one observation.

### 10.9 Missing Values

Missing values occur when some entries in a dataset have no recorded value.

Example:

| Size | Bedrooms | Price |
|---:|---:|---:|
| 1000 | 2 | 5000000 |
| 1500 | NaN | 7000000 |
| 2000 | 4 | 9000000 |

Here, `NaN` indicates a missing value.

Missing values can be handled by:
- Removing affected rows or columns when appropriate.
- Filling numerical values with the mean or median.
- Filling categorical values with the mode.
- Using other suitable imputation techniques.

### 10.10 Outliers

Outliers are observations that differ substantially from the general pattern of the data.

Example:

`5000000, 5500000, 6000000, 100000000`

The value `100000000` is much higher than the other values and may be an outlier.

However, an outlier is not always an error. It should be investigated before deciding whether to keep or remove it.

### 10.11 Data Types

Data types describe the kind of information stored in a column.

Common data types include:

- **Integer:** Whole numbers, such as `25`.
- **Float:** Decimal numbers, such as `25.5`.
- **String:** Text, such as `"Pakistan"`.
- **Boolean:** True or False values.
- **Date/Time:** Dates and times, such as `2026-10-26`.

### 10.12 Categorical Data

Categorical data represents groups, classes, or categories.

Examples:
- City: Multan, Lahore, Karachi.
- Color: Red, Blue, Green.
- House type: Apartment, House, Villa.

Categorical data may need to be converted into numerical representations before being used by certain machine learning algorithms.

### 10.13 Numerical Data

Numerical data represents quantities or measurable values.

Examples:
- Age: `25`
- Salary: `75000`
- House price: `5000000`
- Temperature: `32.5`

Numerical data can be divided into two types:

- **Discrete:** Countable values, such as the number of bedrooms.
- **Continuous:** Measurable values, such as house size or temperature.

### 10.14 Training Dataset

The training dataset is the portion of the data used to teach a machine learning model.

The model learns patterns and relationships from this data.

### 10.15 Validation Dataset

The validation dataset is used to evaluate model performance during development, compare models, and tune hyperparameters.

### 10.16 Test Dataset

The test dataset is used to evaluate the final model on data that was not used for training or tuning.

It helps estimate how well the model performs on unseen data.

### Example of Dataset Splitting

Suppose a dataset contains 1000 house records.

| Dataset | Percentage | Records | Purpose |
|---|---:|---:|---|
| Training | 70% | 700 | Train the model |
| Validation | 15% | 150 | Tune and compare models |
| Testing | 15% | 150 | Evaluate the final model |

This is one possible split. The appropriate proportions depend on the dataset and problem.

### 10.17 Data Preprocessing

Data preprocessing is the process of preparing raw data before using it to train a machine learning model.

Common preprocessing steps include:
- Handling missing values.
- Removing duplicate records when appropriate.
- Investigating outliers.
- Encoding categorical variables.
- Scaling numerical features when needed.
- Splitting data into training, validation, and test sets.

### 10.18 Data Leakage

Data leakage occurs when information that would not legitimately be available at prediction time influences model training or evaluation.

It can make a model appear more accurate than it will be in real-world use.

Example: If a feature contains information derived from the actual future house price, the model may indirectly receive the answer it is supposed to predict.

To prevent data leakage, split the data appropriately and fit preprocessing steps using only the training data.

