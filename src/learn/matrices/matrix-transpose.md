# Matrix transpose

A surprisingly useful operation on matrices is to make the first row into the
first column, the second row into the second column, and so on. This is called
**transposition** and is denoted by $A^{T}$. We say that this is the
**transpose** of $A$.

For a $2 \times 2$ matrix, this looks like

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}^{T}
= \begin{bmatrix} a & c \\ b & d \end{bmatrix}
$$

There are at least three things worth noticing:

1. The first column also becomes the first row, and so on

1. In fact, $A^{T}_{ij}$ is equal to $A_{ji}$

1. Transposition undoes itself: $\left( A^T \right) ^T = A$

You can check all of these things in the $2 \times 2$ case. I'm going to make a
cup of tea, so you have a few minutes.

Righto, let's put transposition into our class.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_transpose

<<< @/../pycode/models/matrix.py#matrix_transpose

:::

## Exercise

<Exercise id="matrix-transpose" />
