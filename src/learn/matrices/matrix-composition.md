# Matrix composition

Since any matrix defines a function $\vec{v} \mapsto A\vec{v}$, we want the
product of two matrices to be equivalent to composition of the functions they
define. In other words, $AB$ had better satisfy

$$
\left( A B \right) \vec{v} = A \left(B \vec{v} \right)
$$

Or, in words, transforming $\vec{v}$ by the product of $A$ and $B$ is the same
as transforming $\vec{v}$ by $B$ and then by $A$. This is entirely analagous to
composition in functional programming:

```python
def compose(f, g):
    return lambda x: f(g(x))
```

To make this work, we need the $i,j$ entry of $AB$ to be the
[dot product](../vectors/dot-product) between the $i^{\text{th}}$ row of $A$ and
the $j^{\text{th}}$ column of $B$.

For $2 \times 2$ matrices, this looks like

$$
\left[
\begin{array}{cc}
a & b \\
c & d
\end{array}
\right]
\left[
\begin{array}{cc}
\alpha & \beta \\
\gamma & \delta
\end{array}
\right]
=
\left[
\begin{array}{cc}
a \alpha + b \gamma &
a \beta + b \delta \\
c \alpha + d \gamma &
c \beta + d \delta
\end{array}
\right]
$$

::: details

Let

$$
A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\quad
B = \begin{bmatrix} \alpha & \beta \\ \gamma & \delta \end{bmatrix}
\quad
v = \begin{bmatrix} x \\ y \end{bmatrix}
$$

Then

$$
\begin{aligned}

\left( A B \right) \vec{v} & = A \left(B \vec{v} \right) \\[5pt]

& = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} \alpha x + \beta y \\ \gamma x + \delta y \end{bmatrix} \\[5pt]

& = \begin{bmatrix}
a \alpha x + a \beta y + b \gamma x + b \delta y \\
c \alpha x + c \beta y + d \gamma x + d \delta y
\end{bmatrix} \\[5pt]

& = \begin{bmatrix}
(a \alpha + b \gamma) x + (a \beta + b \delta) y \\
(c \alpha + d \gamma) x + (c \beta + d \delta) y
\end{bmatrix} \\[5pt]

& = \begin{bmatrix}
a \alpha + b \gamma & a \beta + b \delta \\
c \alpha + d \gamma & c \beta + d \delta
\end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} \\

\end{aligned}
$$

And so, if we want $AB$ to have any meaning, it must be the matrix in the final
line of this calculation.

:::

If we let the rows of $A$ be the vectors $\vec{r_i}$ and the columns of $B$ be
the vectors $\vec{c_j}$, we get the rather pleasing

$$
AB =
\begin{bmatrix}
\vec{r_1} \cdot \vec{c_1} & \vec{r_1} \cdot \vec{c_2} \\
\vec{r_2} \cdot \vec{c_1} & \vec{r_2} \cdot \vec{c_2}
\end{bmatrix}
$$

I'll use this idea in my implementation so I don't end up duplucating my
implementation of the dot product. I'll use the `@` operator for the matrix
product, as intended in Python.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_matrix_product

<<< @/../pycode/models/matrix.py#matrix_matrix_product

:::

::: warning

Matrix composition can only work if the number of columns in $A$ is equal to the
number of rows in $B$, otherwise we cannot take the dot product between a row of
$A$ and a column of $B$.

:::

We had better make sure our matrix product does actually result in the
composition of functions.

<<< @/../pycode/models/matrix_test.py#test_matrix_composition

We don't need to implement anything - our definition of matrix multiplication
already guarantees it will pass.
