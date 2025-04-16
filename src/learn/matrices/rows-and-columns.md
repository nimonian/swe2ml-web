# Rows and columns

A matrix feels a bit like a supervector. Instead of just one column, we get as
many as we want:

$$
A = \begin{bmatrix}
2 & -5 \\
0 & 3 \\
7 & 1
\end{bmatrix}

\quad

B = \begin{bmatrix}
1 & 0 & -2 \\
5 & -3 & 4
\end{bmatrix}
$$

However, we can't go too wild: a matrix must always be rectangular.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_init

<<< @/../pycode/models/matrix.py#matrix_init

:::

We always refer to matrix dimensions by **row** and then by **column**. So $A$
is a $3 \times 2$ matrix, and $B$ is a $2 \times 3$ matrix.

::: tip

An $m \times n$ matrix has $m$ rows and $n$ columns. Row, then column.

:::

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_shape

<<< @/../pycode/models/matrix.py#matrix_shape

:::

The entry in row $i$ and column $j$ is denoted by $A_{ij}$, with $A_{11}$ being
the top-left entry, so

$$
\quad A_{12} = -5, \quad B_{23} = 4
$$

Notice that this notation also follows the convention of row first, then column.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_entry

<<< @/../pycode/models/matrix.py#matrix_entry

:::

::: warning

Again, you will notice that $A_{12}$ is given by `A[0, 1]`, and so on. One day
the rapture will come and set us free. Until then, we just have to suck it up.

:::

Unlike vectors, which we can imagine as being arrows in space (if we want), we
can't really visualise a matrix. As we will learn in the next section, a matrix
represents an **action** rather than a **thing**.

## Exercise

<Exercise id="rows-and-columns" />
