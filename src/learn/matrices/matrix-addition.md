# Matrix addition

To add together two matrices, we just add the entries that occupy the same
position:

$$
\begin{bmatrix} a & b \\ c & d \end{bmatrix}
+ \begin{bmatrix} \alpha & \beta \\ \gamma & \delta \end{bmatrix}

=

\begin{bmatrix} a + \alpha & b + \beta \\ c + \gamma & d + \delta \end{bmatrix}
$$

For example,

$$
\begin{aligned}
\begin{pmatrix}
3 & -1 \\
4 & 2
\end{pmatrix}
+
\begin{pmatrix}
5 & 0 \\
-2 & 7
\end{pmatrix}
& =
\begin{pmatrix}
3 + 5 & -1 + 0 \\
4 - 2 & 2 + 7
\end{pmatrix} \\
& =
\begin{pmatrix}
8 & -1 \\
2 & 9
\end{pmatrix}
\end{aligned}
$$

It seems obvious enough. But, why is this the most sensible way of defining
matrix addition? The point is, we want to make sure that

$$
(A + B) \vec{v} = A \vec{v} + B \vec{v}
$$

because, without this rule, lots of stuff breaks. If you want to see why the
definition of matrix addition is forced on us by the above equation, pop open
the details.

::: details

As we often do, I'm just sticking to $2 \times 2$ matrices here, but all the
work generalises to any shape of matrix.

$$
\begin{aligned}

(A + B) \vec{v}

& = A \vec{v} + B\vec{v} \\

& =
\begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
+ \begin{bmatrix} \alpha & \beta \\ \gamma & \delta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} \\

& =
\begin{bmatrix} ax + by \\ cx + dy \end{bmatrix} +
\begin{bmatrix} \alpha x + \beta y \\ \gamma x + \delta y \end{bmatrix} \\

& =
\begin{bmatrix} ax + by + \alpha x + \beta y \\ cx + dy + \gamma x + \delta y \end{bmatrix} \\

& =
\begin{bmatrix} (a + \alpha)x + (b + \beta)y \\ (c + \gamma)x + (d + \delta)y \end{bmatrix} \\

& =
\begin{bmatrix} a + \alpha & b + \beta \\ c + \gamma & d + \delta \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
\end{aligned}
$$

:::

So we don't really have much choice in the matter - matrix addition must be
defined entrywise. You'll also be thrilled to know that $A + B = B + A$.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_addition

<<< @/../pycode/models/matrix.py#matrix_addition

:::

## Exercise

<Exercise id="matrix-addition" />
