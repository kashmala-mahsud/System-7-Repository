# Day 3: Linear Algebra Basics

## 1. What Is Linear Algebra?

Linear Algebra is a branch of mathematics that deals with vectors, matrices, and linear equations.

It is widely used in Machine Learning, Deep Learning, Computer Vision, and Natural Language Processing.

**Examples of Linear Algebra in Machine Learning:**
- Representing data as vectors and matrices.
- Performing mathematical calculations on datasets.
- Calculating similarities between vectors.
- Representing word embeddings in Natural Language Processing.
- Performing computations inside neural networks.

**In simple words:** Linear Algebra helps us represent and process numerical data efficiently.

---

## 2. What Is a Vector?

A **vector** is an ordered collection of numerical values.

A vector can represent the features of an object, a point in space, or a mathematical quantity.

### Example

Consider a vector:

`v = [2, 4, 6]`

This vector contains three values.

We can represent it mathematically as:

v = [2, 4, 6]

Here:
- The first element is `2`.
- The second element is `4`.
- The third element is `6`.
- The vector has three dimensions.

### Vector Example in Machine Learning

Suppose we want to represent a house using its features.

| Feature | Value |
|---|---:|
| Bedrooms | 3 |
| Bathrooms | 2 |
| Size (hundreds of sq. ft.) | 15 |

The house can be represented as a vector:

`house = [3, 2, 15]`

Each value represents one feature of the house.

### Types of Vectors

**1. Row Vector**

A row vector contains values arranged horizontally.

Example:

`v = [1, 2, 3]`

**2. Column Vector**

A column vector contains values arranged vertically.

Example:

```text
    [1]
v = [2]
    [3]
```

### Basic Vector Operations

#### A. Vector Addition

Vector addition means adding the corresponding elements of two vectors.

Example:

`a = [1, 2, 3]`

`b = [4, 5, 6]`

Addition:

`a + b = [1+4, 2+5, 3+6]`

Result:

`a + b = [5, 7, 9]`

**Important:** Both vectors must have the same number of elements for ordinary vector addition.

#### B. Vector Subtraction

Vector subtraction means subtracting corresponding elements.

Example:

`a = [5, 7, 9]`

`b = [1, 2, 3]`

Subtraction:

`a - b = [5-1, 7-2, 9-3]`

Result:

`a - b = [4, 5, 6]`

#### C. Scalar Multiplication

Scalar multiplication means multiplying every element of a vector by a single number.

Example:

`v = [1, 2, 3]`

Scalar = `2`

Calculation:

`2 * v = [2*1, 2*2, 2*3]`

Result:

`2 * v = [2, 4, 6]`

### Uses of Vectors in Machine Learning

- Representing the features of houses.
- Representing numerical information about customers.
- Storing word embeddings.
- Representing image features.
- Calculating similarity between data points.

---

## 3. What Is a Matrix?

A **matrix** is a rectangular arrangement of numbers organized into rows and columns.

Matrices are used to represent datasets and perform mathematical operations efficiently.

### Example

Consider the following matrix:

```text
A = [1  2  3
     4  5  6]
```

This matrix contains:
- 2 rows.
- 3 columns.
- 6 elements.

Therefore, its shape is:

`(2, 3)`

The shape is written as:

`(number of rows, number of columns)`

### Matrix Example in Machine Learning

Suppose we have information about three houses.

| House | Bedrooms | Bathrooms | Size (hundreds of sq. ft.) |
|---|---:|---:|---:|
| House 1 | 2 | 1 | 10 |
| House 2 | 3 | 2 | 15 |
| House 3 | 4 | 3 | 20 |

We can represent the data as a matrix:

```text
X = [2  1  10
     3  2  15
     4  3  20]
```

The matrix has three rows and three columns.

Its shape is:

`(3, 3)`

Here:
- Each row represents one house.
- Each column represents one feature.

This is a common way to represent feature data in Machine Learning.

### Types of Matrices

**1. Row Matrix**

A matrix with only one row.

Example:

```text
A = [1  2  3]
```

Shape: `(1, 3)`

**2. Column Matrix**

A matrix with only one column.

Example:

```text
A = [1
     2
     3]
```

Shape: `(3, 1)`

**3. Square Matrix**

A matrix with the same number of rows and columns.

Example:

```text
A = [1  2
     3  4]
```

Shape: `(2, 2)`

**4. Zero Matrix**

A matrix in which every element is zero.

Example:

```text
A = [0  0
     0  0]
```

**5. Identity Matrix**

A square matrix with ones on the main diagonal and zeros everywhere else.

Example:

```text
I = [1  0  0
     0  1  0
     0  0  1]
```

Multiplying a compatible matrix by an identity matrix leaves the original matrix unchanged.

### Basic Matrix Operations

#### A. Matrix Addition

Matrix addition means adding corresponding elements of two matrices with the same shape.

Example:

```text
A = [1  2
     3  4]

B = [5  6
     7  8]
```

Addition:

```text
A + B = [1+5  2+6
         3+7  4+8]
```

Result:

```text
A + B = [ 6   8
         10  12]
```

#### B. Matrix Subtraction

Matrix subtraction means subtracting corresponding elements of two matrices with the same shape.

Example:

```text
A = [5  6
     7  8]

B = [1  2
     3  4]
```

Result:

```text
A - B = [4  4
         4  4]
```

#### C. Scalar Multiplication

Scalar multiplication means multiplying every element of a matrix by the same number.

Example:

```text
A = [1  2
     3  4]
```

Multiply by `2`:

```text
2A = [2  4
      6  8]
```

### Uses of Matrices in Machine Learning

- Representing datasets with multiple observations and features.
- Storing image pixels.
- Performing calculations in neural networks.
- Representing batches of input data.
- Transforming numerical data.

---

## 4. What Is a Dot Product?

The **dot product** is a mathematical operation that multiplies the corresponding elements of two vectors and then adds the results.

It is also called the scalar product because the result is a single number.

### Formula

For two vectors:

`a = [a1, a2, a3]`

`b = [b1, b2, b3]`

The dot product is:

`a . b = (a1*b1) + (a2*b2) + (a3*b3)`

In general:

`a . b = sum(a[i] * b[i])`

### Example

Consider two vectors:

`a = [1, 2, 3]`

`b = [4, 5, 6]`

Step 1: Multiply corresponding elements.

- `1 * 4 = 4`
- `2 * 5 = 10`
- `3 * 6 = 18`

Step 2: Add the results.

`a . b = 4 + 10 + 18`

`a . b = 32`

**Answer: Dot Product = 32**

### Dot Product Example in Machine Learning

Suppose we want to estimate a house price using two features:

- House size = 1000 square feet.
- Number of bedrooms = 3.

For illustration, suppose the model uses these weights:

- Size weight = 2000.
- Bedroom weight = 50000.

Represent the features as a vector:

`x = [1000, 3]`

Represent the weights as a vector:

`w = [2000, 50000]`

Calculate the dot product:

`x . w = (1000 * 2000) + (3 * 50000)`

`x . w = 2000000 + 150000`

`x . w = 2150000`

The weighted sum is `2,150,000`.

This is an illustrative linear model without a bias term. A real model learns suitable weights from training data and may also include a bias term.

### Why Is the Dot Product Important?

- Calculating weighted sums in linear models.
- Computing similarities between vectors.
- Performing calculations in neural networks.
- Working with word embeddings.
- Supporting recommendation systems.

### Important Condition

Two vectors must have the same number of elements to calculate their dot product.

For example:

`[1, 2, 3] . [4, 5, 6]`

is valid because both vectors contain three elements.

However:

`[1, 2] . [3, 4, 5]`

is not a valid dot product because the vectors have different lengths.

---

## 5. Difference Between Vectors, Matrices, and Dot Products

| Concept | Definition | Example | Common Use |
|---|---|---|---|
| Vector | An ordered collection of numbers | `[1, 2, 3]` | Representing features |
| Matrix | A rectangular arrangement of numbers | `[[1, 2], [3, 4]]` | Representing datasets |
| Dot Product | Multiplying corresponding vector elements and adding the results | `[1, 2] . [3, 4] = 11` | Weighted sums and similarity calculations |

---