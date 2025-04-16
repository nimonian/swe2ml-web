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

For example, let's calculate

$$
\begin{bmatrix}
1 & 2 \\
3 & 4
\end{bmatrix}
\begin{bmatrix}
5 \\ 6
\end{bmatrix}
=
\begin{bmatrix}
? \\ ?
\end{bmatrix}
$$

First, we take the dot product using the first row,

$$
\begin{aligned}
\begin{bmatrix}
\class{hl-red}{1} & \class{hl-red}{2} \\
3 & 4
\end{bmatrix}
\begin{bmatrix}
\class{hl-red}{5} \\ \class{hl-red}{6}
\end{bmatrix}
& =
\begin{bmatrix}
\class{hl-red}{1 \times 5 + 2 \times 6} \\
?
\end{bmatrix} \\
& =
\begin{bmatrix}
17 \\ ?
\end{bmatrix}
\end{aligned}
$$

Then, we do the same with the second row:

$$
\begin{aligned}
\begin{bmatrix}
1 & 2 \\
\class{hl-red}{3} & \class{hl-red}{4}
\end{bmatrix}
\begin{bmatrix}
\class{hl-red}{5} \\ \class{hl-red}{6}
\end{bmatrix}
& =
\begin{bmatrix}
17 \\
\class{hl-red}{3 \times 5 + 4 \times 6}
\end{bmatrix} \\
& = \begin{bmatrix}
17 \\
39
\end{bmatrix}
\end{aligned}
$$

And so the vector $\begin{bmatrix} 5 \\ 6 \end{bmatrix}$ is mapped to the vector
$\begin{bmatrix} 17 \\ 39 \end{bmatrix}$ under the transformation
$\begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$.

::: warning

Multiplying a matrix with a vector only works if the number of **columns in the
matrix** is equal to the number of **components in the vector**. If the
dimensions aren't right, we can't do the dot product between row and vector.

:::

We also find that this definition of matrix-vector multiplication satisfies an
important "distributive law":

$$
A \left( \vec{u} + \vec{v} \right) = A \vec{u} + A \vec{v}
$$

With this, we should be able to implement multiplying a vector by a matrix.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_vector_multiplication

<<< @/../pycode/models/matrix.py#matrix_vector_multiplication

:::

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
