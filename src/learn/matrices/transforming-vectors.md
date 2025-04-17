# Transforming vectors

In [rows and columns](./rows-and-columns), we said that a matrix represents an
**action** rather than a thing. So, what actions do they represent, and what
things do they act on?

You have probably guessed by the title that matrices act on vectors. We can
calculate the **product** of a matrix with a vector to get a new vector. To get
the components of this new vector, we take the
[dot product](../vectors/dot-product) with **each row** of the matrix.

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} ax + by \\ cx + dy \end{bmatrix}
$$

For example, let's say

$$
A = \begin{bmatrix}
2 & -1 \\ 0 & 3
\end{bmatrix},

\quad

\vec{v} = \begin{bmatrix}
4 \\ 5
\end{bmatrix}
$$

and we want to calculate $A \vec{v}$. First, we take the dot product using the
first row,

$$
\left[
\begin{array}{cc}
\rowcolor{gray} 2 & -1 \\
0 & 3
\end{array}
\right]

\left[
\begin{array}{c}
\columncolor{gray}
4 \\ 5
\end{array}
\right]

=

\left[
\begin{array}{c}
\rowcolor{gray} 8 - 5 \\ \,
\end{array}
\right]

=
\begin{bmatrix}
3 \\ \,
\end{bmatrix}
$$

Then with the second row,

$$
\left[
\begin{array}{cc}
2 & -1 \\
\rowcolor{gray} 0 & 3
\end{array}
\right]

\left[
\begin{array}{c}
\columncolor{gray}
4 \\ 5
\end{array}
\right]

=

\left[
\begin{array}{c}
3 \\
\rowcolor{gray} 0 + 15
\end{array}
\right]

=

\begin{bmatrix}
3 \\ 15
\end{bmatrix}
$$

::: warning

Multiplying a matrix with a vector only works if the number of **columns in the
matrix** is equal to the number of **components in the vector**. If the
dimensions aren't right, we can't do the dot product between row and vector.

:::

With this, we should be able to implement multiplying a vector by a matrix.
Similar to the dot product of two vectors, we will make use of Python's `@`
infix operator with `__matmul__`.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_vector_multiplication

<<< @/../pycode/models/matrix.py#matrix_vector_multiplication

:::

We also find that this definition of matrix-vector multiplication satisfies an
important "distributive law":

$$
A \left( \vec{u} + \vec{v} \right) = A \vec{u} + A \vec{v}
$$

<<< @/../pycode/models/matrix_test.py#test_matrix_left_distributivity

We don't need to implement anything here - it's guaranteed by the definition of
matrix multiplication.

If a matrix is square, then it doesn't affect the dimension of the vector.
However, a non-square matrix will indeed change the dimension of the vector. For
example,

$$
\begin{bmatrix}
3 & 1 & -2 \\
1 & -4 & 0
\end{bmatrix}

\begin{bmatrix}
5 \\ -3 \\ 1
\end{bmatrix}

=

\begin{bmatrix}
10 \\ 17
\end{bmatrix}
$$

Actually, if you think about it, the number of rows in the matrix equals the
dimension of the output. And if you don't think about it, the number of rows in
the matrix still equals the dimension of the output.

## Exercise

<Exercise id="transforming-vectors" />
