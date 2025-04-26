# The cross product

The cross product is a strange one: given vectors $\vec{u}$ and $\vec{v}$ in $3$
dimensions, it returns a vector $\vec{n} = \vec{u} \times \vec{v}$ which is
perpendicular (or _normal_) to both of them.

![](../../images/cross-prod-normal.svg)

It turns out that the correct components for this vector are

$$
\vec{u} \times \vec{v} =
\begin{bmatrix}
u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1
\end{bmatrix}
$$

::: details

To ensure that $\vec{n}$ is perpendicular to $\vec{u}$ and $\vec{v}$, it is
enough to make sure that the dot product is $0$:

$$
\begin{aligned}
\vec{n} \cdot \vec{u} & = 0 \\
\vec{n} \cdot \vec{v} & = 0
\end{aligned}
$$

In terms of components, this means we need

$$
\begin{aligned}
n_1 u_1 + n_2 u_2 + n_3 u_3 & = 0 \\
n_1 v_1 + n_2 v_2 + n_3 v_3 & = 0
\end{aligned}
$$

We're going to solve, using simultaneous equations, to find $\vec{n}$. First up,
let's eliminate $n_2$ by multiplying the top equation by $v_2$ and the bottom
equation by $u_2$, then subtracting.

$$
\begin{aligned}
&& n_1 u_1 v_2 + n_2 u_2 v_2 + n_3 u_3 v_2 & = 0 \\
(-) && n_1 u_2 v_1  + n_2 u_2 v_2 + n_3 u_2 v_3 & = 0 \\
\Rightarrow && n_1 (u_1 v_2 - u_2 v_1) + n_3 (u_3 v_2 - u_2 v_3) & = 0
\end{aligned}
$$

Rearranging, we find

$$
n_1 = n_3 \frac{u_2 v_3 - u_3 v_2}{u_1 v_2 - u_2 v_1}
$$

I'll omit some of the details, but you may check that eliminating $n_1$ also
gives

$$
n_2 = n_3 \frac{u_3 v_1 - u_1 v_3}{u_1 v_2 - u_2 v_1}
$$

Since there are two equations and three unknowns, we can let $n_3$ be anything
we like. As you can see, it would be most convenient if
$n_3 = u_1 v_2 - u_2 v_1$, in which case we get

$$
\vec{n} = \begin{bmatrix}
u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1
\end{bmatrix}
$$

:::

Let's get this into our class before my head explodes.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_cross_product

<<< @/../pycode/models/vector.py#vector_cross_product

:::

## Exercise

<Exercise id="cross-product" />
