# Scaling matrices

Whilst we're on the subject, we might as well make sure that we can multiply a
matrix by a number. To make this useful, we'd want to ensure that

$$
\lambda \left( A \vec{v} \right) = \left( \lambda A \right) \vec{v}
$$

We know how to work out the left hand side, because $A\vec{v}$ is just a vector,
and [scaling a vector](../vectors/scaling-vectors) is already defined. To make
sure the right hand side works out to be the same thing, we have to define

$$
\lambda
\begin{bmatrix}
a & b \\ c & d
\end{bmatrix}
=
\begin{bmatrix}
\lambda a & \lambda b \\ \lambda c & \lambda d
\end{bmatrix}
$$

::: details

$$
\begin{aligned}

\left( \lambda A \right) \vec{v}

& = \lambda \left( A \vec{v} \right) \\

& =
\lambda
\begin{bmatrix}
ax + by \\ cx + dy
\end{bmatrix} \\

& =
\begin{bmatrix}
\lambda ax + \lambda by \\ \lambda cx + \lambda dy
\end{bmatrix} \\

& =
\begin{bmatrix}
\lambda a & \lambda b \\ \lambda c & \lambda d
\end{bmatrix}
\begin{bmatrix}
x \\ y
\end{bmatrix}

\end{aligned}
$$

So the matrix in the final line of this calculation **has** to be the way we
define $\lambda A$.

:::

This definition for $\lambda A$ also agrees with the very common sense

$$
A + A = 2A
$$

which is a huge relief.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_scalar_multiplication

<<< @/../pycode/models/matrix.py#matrix_scalar_multiplication

:::

We also get matrix subtraction for free:

$$
A - B = A + (-B)
$$

::: code-group

<<< @/../pycode/models/matrix_test.py#test_matrix_subtraction

<<< @/../pycode/models/matrix.py#matrix_subtraction

:::

## Exercise

<Exercise id="scaling-matrices" />

(If you want to be especially sneaky, you might even avoid calculating all of
$C$ and just focus on the one entry you really care about.)
