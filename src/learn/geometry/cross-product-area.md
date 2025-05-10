# Cross product area property

There's another thing we need to know about the cross product

$$
\vec{u} \times \vec{v} = \begin{bmatrix}
u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1
\end{bmatrix}
$$

The magnitude

$$
|\vec{u} \times \vec{v}| = \sqrt{(u_2 v_3 - u_3 v_2)^2 + (u_3 v_1 - u_1 v_3)^2 + (u_1 v_2 - u_2 v_1)^2}
$$

is actually the area $|\vec{u}||\vec{v}|\sin\theta$ of the parallelogram spanned
by $\vec{u}$ and $\vec{v}$.

![](../../images/plane-3d.svg)

To see why, there's a pretty neat formula that gives the area of the
parallelogram spanned by two vectors in any dimension:

$$
\text{Area} = \sqrt{|\vec{u}|^2 |\vec{v}|^2 - \left(\vec{u} \cdot \vec{v}\right)^2}
$$

::: details

$$
\begin{aligned}
\text{Area}^2
& = |\vec{u}|^2 |\vec{v}|^2 \sin^2 \theta \\
& = |\vec{u}|^2 |\vec{v}|^2 \left( 1 - \cos^2 \theta \right) \\
& = |\vec{u}|^2 |\vec{v}|^2 + |\vec{u}|^2 |\vec{v}|^2 \cos^2 \theta \\
& = |\vec{u}|^2 |\vec{v}|^2 - \left(\vec{u} \cdot \vec{v} \right)^2 \\
\end{aligned}
$$

:::

In two dimensions, this agrees with our
[parallelogram formula](./parallelograms.md) $\vec{u} \cdot \vec{v}_{\perp}$.

::: details

$$
\begin{aligned}
\text{Area}^2
& = (\vec{u} \cdot \vec{u}) (\vec{v} \cdot \vec{v}) - (\vec{u} \cdot \vec{v})^2 \\
& = (u_1^2 + u_2^2)(v_1^2 + v_2)^2 - (u_1 v_1 + u_2 v_2)^2 \\
& = \cancel{u_1^2 v_1^2} + u_1^2 v_2^2 + u_2^2 v_1^2 + \cancel{u_2^2 v_2^2}
- \cancel{u_1^2 v_1^2} - 2 u_1 v_2 u_2 v_1 - \cancel{u_2^2 v_2^2} \\
& = (u_1 v_2 - u_2 v_1)^2
\end{aligned}
$$

:::

In three dimensions, this works out to be exactly the magnitude
$|\vec{u} \times \vec{v}|$.

::: details

Get ready...

$$
\begin{aligned}
\text{Area}^2
& = |\vec{u}|^2 |\vec{v}|^2 - \left(\vec{u} \cdot \vec{v} \right)^2 \\

& = \left( u_1^2 + u_2^2 + u_3^2
\right)\left( v_1^2 + v_2^2 + v_3^2 \right) - \left( u_1v_1 + u_2v_2 + u_3v_3
\right)^2 \\

& = \cancel{u_1^2 v_1^2} + u_1^2 v_2^2 + u_1^2 v_3^2 + u_2^2
v_1^2 + \cancel{u_2^2 v_2^2} + u_2^2 v_3^2 + u_3^2 v_1^2 + u_3^2 v_2^2 +
\cancel{u_3^2 v_3^2} \\

& \quad - \cancel{u_1^2 v_1^2} - \cancel{u_2^2 v_2^2} -
\cancel{u_3^2 v_3^2} - 2\left( u_2v_2u_3v_3 + u_3v_3u_1v_1 + u_1v_1u_2v_2
\right) \\

& =( u_2^2 v_3^2 + u_3^2 v_2^2 - 2 u_2 v_2 u_3 v_3) + (u_3^2 v_1^2 + u_1^2 v_3^2 - 2 u_3 v_3 u_1 v_1)  \\
& \quad + (u_1^2 v_2^2 + u_2^2 v_1^2 - 2 u_1v_1u_2v_2) \\

& = (u_2 v_3 - u_3 v_2)^2 + (u_3 v_1 - u_1 v_3)^2 + (u_1 v_2 - u_2 v_1)^2 \\

& = | \vec{u} \times \vec{v} |^2
\end{aligned}
$$

Phew!

:::

::: tip

The cross product $\vec{u} \times \vec{v}$ is the vector $\vec{n}$ which is
normal to $\vec{u}$ and $\vec{v}$, and whose magnitude is equal to the area
spanned by $\vec{u}$ and $\vec{v}$.

:::

## Code

Let's go ahead and implement the rather beautiful formula
$|\vec{u}|^2 |\vec{v}|^2 - \left(\vec{u} \cdot \vec{v} \right)^2$ which works
for any dimension, so long as we have two vectors.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_area

<<< @/../pycode/models/vector.py#vector_area

:::

The second assertion here, though, is what this page is really all about.
