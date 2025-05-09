# Identity matrix

The matrices

$$
I_2 = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}, \quad I_3 = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad \ldots
$$

are called the **identity** matrices. They leave any vector completely
unchanged:

$$
\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 2 \end{bmatrix} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}
$$

Generally,

$$
I \, \vec{v} = \vec{v}
$$

Let's chuck a static method into our class to create identity matrices.

::: code-group

<<< @/../pycode/models/matrix_test.py#test_identity_matrix

<<< @/../pycode/models/matrix.py#identity_matrix

:::

There's no exercise here as there's nothing to do, really! It's enough to know
that the identity matrices exist and they come in handy when we're doing algebra
with matrices.

<!-- ## Scaling

Note that

$$
\begin{bmatrix} 7 & 0 \\ 0 & 7 \end{bmatrix} \begin{bmatrix} x \\ y\end{bmatrix} = \begin{bmatrix} 7x \\ 7y \end{bmatrix}
$$

which is basically just the same as scalar multiplication. We will see soon that
it makes sense to write $7I$ to represent this vector, but not straight away as
we haven't even defined the operation of multiplying a matrix by a number yet.

## Reflecting

The matrices

$$
S_x = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix},
\quad S_y = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}
$$

will reflect any $2$-dimensional vector in the $x$-axis and $y$-axis
respectively. To see why, consider

$$
\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x \\ -y \end{bmatrix}
$$

When the $y$-coordinate of a point is replaced with $-y$, the point is being
reflected in the $x$-axis.

![](../../images/reflection-matrix.svg)

## Rotating

The matrix

$$
R_{\theta} = \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
$$

will rotate any $2$ dimensional matrix by $\theta$ in the anticlockwise
direction.

![](../../images/rotation-matrix.svg)

Want to know why?

::: details

Let's label a few things.

![](../../images/rotation-matrix-proof.svg)

By basic trigonometry,

$$
\begin{aligned}
x & = |\vec{v}| \cos \varphi \\
y & = |\vec{v}| \sin \varphi \\
\end{aligned}
$$

Let's calculate $x'$:

$$
\begin{aligned}
x'
& = |\vec{v}| \cos(\varphi + \theta) \\
& = |\vec{v}| (\cos \varphi \cos \theta - \sin \varphi \sin \theta) \\
& = |\vec{v}| \cos \varphi \cos \theta - |\vec{v}| \sin \varphi \sin \theta \\
& = x \cos \theta - y \sin \theta
\end{aligned}
$$

And $y'$:

$$
\begin{aligned}
y'
& = |\vec{v}| \sin(\varphi + \theta) \\
& = |\vec{v}| (\cos \varphi \sin \theta + \sin \varphi \cos \theta) \\
& = |\vec{v}| \cos \varphi \sin \theta + |\vec{v}| \sin \varphi \cos \theta \\
& = x \sin \theta + y \cos \theta
\end{aligned}
$$

This tells us that

$$
\begin{aligned}
R_\theta \vec{v}
& = \begin{bmatrix} x' \\ y' \end{bmatrix} \\
& = \begin{bmatrix} x \cos \theta - y \sin \theta \\ x \sin \theta + y \cos \theta \end{bmatrix} \\
& = \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
\end{aligned}
$$

Hence

$$
R_\theta = \begin{bmatrix} \cos \theta & - \sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
$$

:::

## Exercise

<Exercise id="special-transformations" /> -->
