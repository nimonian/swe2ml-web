# Matrix multiplication

We can add together two matrices, and we can multiply a matrix by a number, but
can we multiply two matrices together?

The answer is **yes**, there is a very natural way of defining matrix
multiplication. The $i,j$ entry of $AB$ is the
[dot product](../vectors/dot-product) between the $i^{\text{th}}$ row of $A$ and
the $j^{\text{th}}$ column of $B$.

For $2 \times 2$ matrices, this looks like

$$
\begin{aligned}
\left[
\begin{array}{cc}
\rowcolor{gray} a & b \\
c & d
\end{array}
\right]

\left[
\begin{array}{cc}
\columncolor{gray} \alpha & \beta \\
\gamma & \delta
\end{array}
\right]

& =

\left[
\begin{array}{cc}
\cellcolor{gray} a \alpha + b \gamma &
\quad\quad\quad\, \\
\quad\quad\quad\, &
\quad\quad\quad\,
\end{array}
\right]

\\[6pt]

\left[
\begin{array}{cc}
\rowcolor{gray} a & b \\
c & d
\end{array}
\right]

\left[
\begin{array}{cc}
\alpha & \columncolor{gray} \beta \\
\gamma & \delta
\end{array}
\right]

& =

\left[
\begin{array}{cc}
a \alpha + b \gamma &
\cellcolor{gray} a \beta + b \delta \\
\quad\quad\quad\, &
\quad\quad\quad\,
\end{array}
\right]

\\[6pt]

\left[
\begin{array}{cc}
a & b \\
\rowcolor{gray} c & d
\end{array}
\right]

\left[
\begin{array}{cc}
\columncolor{gray} \alpha & \beta \\
\gamma & \delta
\end{array}
\right]

& =

\left[
\begin{array}{cc}
a \alpha + b \gamma &
a \beta + b \delta \\
\cellcolor{gray} c \alpha + d \gamma &
\,
\end{array}
\right]

\\[6pt]

\left[
\begin{array}{cc}
a & b \\
\rowcolor{gray} c & d
\end{array}
\right]

\left[
\begin{array}{cc}
\alpha & \columncolor{gray} \beta \\
\gamma & \delta
\end{array}
\right]

& =

\left[
\begin{array}{cc}
a \alpha + b \gamma &
a \beta + b \delta \\
c \alpha + d \gamma &
\cellcolor{gray} c \beta + d \delta
\end{array}
\right]
\end{aligned}
$$

Matrix multiplication can only work if the number of columns in $A$ is equal to
the number of rows in $B$, otherwise we cannot take the dot product between a
row of $A$ and a column of $B$. If $A$ is an $m \times n$ matrix and $B$ is a
$p \times q$ matrix, this means we need to have $n = p$.

It also means that the matrix $AB$ is a $m \times q$ matrix. For example, if

$$
A = \begin{bmatrix}
2 & -1 & 4 \\
0 & 3 & 5
\end{bmatrix}

\quad

B = \begin{bmatrix}
1 & 2 \\
-2 & 0 \\
3 & -1
\end{bmatrix}
$$

then

$$
\begin{aligned}
AB

& = \begin{bmatrix}
2 + 2 + 12 & 4 + 0 - 4 \\
0 - 6 + 15 & 0 + 0 - 5
\end{bmatrix} \\

& = \begin{bmatrix}
16 & 0 \\
9 & -5
\end{bmatrix}
\end{aligned}
$$

However, note that generally $AB \neq BA$. If we perform the calculation, we see
that

$$
\begin{aligned}
BA

& = \begin{bmatrix}
2 + 0 & -1 + 6 & 4 + 10 \\
-4 + 0 & 2 + 0 & -8 + 0 \\
6 + 0 & -3 - 3 & 12 - 5
\end{bmatrix} \\

& = \begin{bmatrix}
2 & 5 & 14 \\
-4 & 2 & -8 \\
6 & -6 & 7
\end{bmatrix}
\end{aligned}
$$

Let's get matrix multiplication into our `Matrix` class.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_matrix_multiplication

<<< @/../pycode/models/matrix.py#matrix_matrix_multiplication {1,2,23-32}

:::

::: warning

This is not an efficient implementation of matrix multiplication, because we
have the overhead of converting stuff into `Vector`s. But it's readable and
educational, which is more to the point.

:::

Do you feel that? That creeping sensation? That's the unsettling itch of the
question **why?** Why is this how we multiply matrices? Is this definition just
made up by sadists to torture us? No. Matrix multiplication _has to be this way_
to make sure that

$$
\left( A B \right) \vec{v} = A \left(B \vec{v} \right)
$$

Remember, **matrices transform vectors**. The above equation ensures that
transforming $\vec{v}$ by $B$ and then by $A$, is the same as trasforming
$\vec{v}$ by the composition of $A$ and $B$. To borrow some ideas from
functional programming, it's a bit like saying

```python
assert compose(f, g)(v) == f(g(v))
```

With matrices, rather than functions, we can do a similar test:

<<< @/../pycode/models/matrix_test.py#test_matrix_composition

We don't need to implement anything - our definition of matrix multiplication
already guarantees it will pass. Want to know why?

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

\left( A B \right) \vec{v} & = A \left(B \vec{v} \right) \\

& = \begin{bmatrix} a & b \\ c & d \end{bmatrix}
\begin{bmatrix} \alpha x + \beta y \\ \gamma x + \delta y \end{bmatrix} \\

& = \begin{bmatrix}
a \alpha x + a \beta y + b \gamma x + b \delta y \\
c \alpha x + c \beta y + d \gamma x + d \delta y
\end{bmatrix} \\

& = \begin{bmatrix}
(a \alpha + b \gamma) x + (a \beta + b \delta) y \\
(c \alpha + d \gamma) x + (c \beta + d \delta) y
\end{bmatrix} \\

& = \begin{bmatrix}
a \alpha + b \gamma & a \beta + b \delta \\
c \alpha + d \gamma & c \beta + d \delta
\end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} \\

\end{aligned}
$$

And so, if we want $AB$ to have any meaning, it must be the matrix in the final
line of this calculation.

:::
