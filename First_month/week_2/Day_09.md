## 1. What is Mean?

**Mean** is the average of all values in a dataset. It is calculated by adding all the values and dividing the sum by the total number of values.

### Formula

Mean = Sum of all values / Total number of values

### Example

Consider the following dataset:

`10, 20, 30, 40, 50`

Step 1: Add all the values.

Sum = 10 + 20 + 30 + 40 + 50 = 150

Step 2: Count the total number of values.

Total values = 5

Step 3: Divide the sum by the total number of values.

Mean = 150 / 5 = 30

**Answer: Mean = 30**

### Uses of Mean

- Finding the average marks of students.
- Calculating the average salary of employees.
- Analyzing average house prices.
- Understanding the central value of numerical data.

**Important:** The mean is sensitive to outliers. Extremely large or small values can significantly affect it.

---

## 2. What is Median?

**Median** is the middle value of a dataset when all values are arranged in ascending or descending order.

The median divides the dataset into two halves.

### Case 1: Odd Number of Values

Consider the dataset:

`10, 20, 30, 40, 50`

There are 5 values, so the middle value is 30.

**Answer: Median = 30**

### Case 2: Even Number of Values

Consider the dataset:

`10, 20, 30, 40, 50, 60`

There are 6 values, so we take the average of the two middle values.

Middle values = 30 and 40

Median = (30 + 40) / 2

Median = 70 / 2 = 35

**Answer: Median = 35**

### Uses of Median

- Finding the typical house price in a city.
- Analyzing salaries when some salaries are extremely high.
- Handling numerical data containing outliers.
- Understanding the central value of a dataset.

**Important:** The median is less sensitive to outliers than the mean.

---

## 3. What is Mode?

**Mode** is the value that appears most frequently in a dataset.

A dataset can have one mode, multiple modes, or no mode if all values occur equally often.

### Example 1: One Mode

Consider the dataset:

`10, 20, 20, 30, 40`

The value 20 appears twice, while the other values appear once.

**Answer: Mode = 20**

### Example 2: Two Modes

Consider the dataset:

`10, 10, 20, 30, 30, 40`

The values 10 and 30 both appear twice.

**Answer: Modes = 10 and 30**

This dataset is called bimodal.

### Example 3: No Mode

Consider the dataset:

`10, 20, 30, 40`

Every value appears once, so there is no unique mode.

**Answer: No mode**

### Uses of Mode

- Finding the most common product purchased by customers.
- Identifying the most popular clothing size.
- Finding the most frequently occurring category.
- Analyzing categorical data, such as city names or colors.

**Important:** Unlike mean and median, mode can be used with categorical data.

---

## 4. What is Variance?

**Variance** is a statistical measure that describes how far the values in a dataset are spread out from their mean.

A low variance means that the values are generally close to the mean.

A high variance means that the values are more spread out.

Variance is calculated by finding the squared differences between each value and the mean, then averaging those squared differences.

### Population Variance Formula

Population Variance = Sum of Squared Differences / Total Number of Values

In mathematical notation:

σ² = Σ(xᵢ - μ)² / N

Where:

- σ² = Population variance
- xᵢ = Each value in the dataset
- μ = Population mean
- N = Total number of values
- Σ = Sum of all values

### Example

Consider the dataset:

`2, 4, 6, 8, 10`

**Step 1: Calculate the mean.**

Mean = (2 + 4 + 6 + 8 + 10) / 5

Mean = 30 / 5 = 6

**Step 2: Calculate the difference between each value and the mean.**

| Value (x) | Mean | Difference (x - Mean) |
|---:|---:|---:|
| 2 | 6 | -4 |
| 4 | 6 | -2 |
| 6 | 6 | 0 |
| 8 | 6 | 2 |
| 10 | 6 | 4 |

**Step 3: Square each difference.**

| Value (x) | Difference | Squared Difference |
|---:|---:|---:|
| 2 | -4 | 16 |
| 4 | -2 | 4 |
| 6 | 0 | 0 |
| 8 | 2 | 4 |
| 10 | 4 | 16 |

**Step 4: Add all squared differences.**

Sum = 16 + 4 + 0 + 4 + 16 = 40

**Step 5: Divide by the total number of values.**

Variance = 40 / 5 = 8

**Answer: Population Variance = 8**

### Sample Variance

When data represents a sample from a larger population, sample variance is commonly calculated by dividing the sum of squared differences by N - 1 instead of N.

Sample Variance = Sum of Squared Differences / (N - 1)

For the same dataset:

Sample Variance = 40 / (5 - 1)

Sample Variance = 40 / 4 = 10

**Answer: Sample Variance = 10**

### Uses of Variance

- Measuring the spread of data.
- Understanding variation in house prices.
- Analyzing financial returns.
- Comparing variability between datasets.
- Supporting statistical analysis and machine learning.

**Important:** Variance is expressed in squared units. For example, if the original values are measured in square feet, the variance is measured in square feet squared.

---

## 5. What is Standard Deviation?

**Standard Deviation** is a statistical measure that describes how much the values in a dataset typically vary around the mean.

It is the square root of the variance.

A low standard deviation means that the values are generally close to the mean.

A high standard deviation means that the values are more spread out.

### Formula

Population Standard Deviation = √Population Variance

In mathematical notation:

σ = √(Σ(xᵢ - μ)² / N)

Where:

- σ = Population standard deviation
- xᵢ = Each value in the dataset
- μ = Population mean
- N = Total number of values
- √ = Square root

### Example

Consider the same dataset:

`2, 4, 6, 8, 10`

From the previous example:

Population Variance = 8

Standard Deviation = √8

Standard Deviation ≈ 2.83

**Answer: Population Standard Deviation ≈ 2.83**

For a sample, the sample standard deviation is the square root of the sample variance.

Sample Variance = 10

Sample Standard Deviation = √10 ≈ 3.16

### Uses of Standard Deviation

- Understanding how spread out data values are.
- Measuring variation in house prices.
- Analyzing student marks.
- Detecting unusual observations.
- Understanding data distribution.
- Supporting feature scaling and statistical analysis in machine learning.

**Important:** Standard deviation uses the same units as the original data, making it easier to interpret than variance.

---

