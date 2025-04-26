# Transforming vectors

In [rows and columns](./rows-and-columns), we said that a matrix represents an
**action** rather than a thing. So, what actions do they represent, and what
things do they act on?

You have probably guessed by the title that matrices act on vectors. We can
calculate the **product** of a matrix with a vector to get a new vector. To get
the components of this new vector, we take the
[dot product](../vectors/dot-product) with **each row** of the matrix.

$$
A \vec{v} =
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
=
\begin{bmatrix} ax + by \\ cx + dy \end{bmatrix}
$$

For example,

$$
\begin{bmatrix}
2 & -1 \\ 0 & 3
\end{bmatrix}

\begin{bmatrix}
4 \\ 5
\end{bmatrix}

= \begin{bmatrix}
8 - 5 \\ 0 + 15
\end{bmatrix}

= \begin{bmatrix}
3 \\ 15
\end{bmatrix}
$$

For me, it helps to think of the rows of the matrix as vectors $\vec{r_i}$
(albeit written horizontally):

$$
A\vec{v}

= \begin{bmatrix} \vec{r_1} \cdot \vec{v} \\ \vec{r_2} \cdot \vec{v} \\ \vdots \\ \vec{r_m} \cdot \vec{v} \end{bmatrix}
$$

In fact, this is how I'll implement matrices acting on vectors in the code.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_vector_transformation

<<< @/../pycode/models/matrix.py#matrix_vector_transformation

:::

::: warning

Transforming a vector by a matrix only works if the number of **columns in the
matrix** is equal to the number of **components in the vector**. If the
dimensions aren't right, we can't do the dot product between row and vector.

:::

We also find that this definition of matrix-vector transformation satisfies an
important "distributive law":

$$
A \left( \vec{u} + \vec{v} \right) = A \vec{u} + A \vec{v}
$$

<<< @/../pycode/models/matrix_test.py#test_matrix_left_distributivity

We don't need to implement anything here - it's guaranteed by the operation of
vector transformation.

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
