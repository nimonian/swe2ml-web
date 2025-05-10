# Parallelograms

Given two vectors, we can create a parallelogram like this:

![](../../images/vector-parallelogram.svg)

The area of the parallelogram can be found, through elementary geometry, to be

$$
\text{Area} = |\vec{u}| |\vec{v}| \sin \theta
$$

I still can't find my protractor. Fortunately, I don't need it, because this
area can be expressed purely in terms of the components of the vectors! It is

$$
\text{Area} = u_1 v_2 - u_2 v_1
$$

::: details

Check this picture out:

![](../../images/cross-prod-proof.svg)

We find the area of the surrounding rectangle in two ways.

On the one hand, it is clearly

$$
u_1 v_2
$$

On the other hand, we can add up the four triangles, so

$$
\begin{aligned}
u_1 v_2 & = \frac{u_1 u_2}{2} + \frac{v_1 v_2}{2} + \frac{(u_1 - v_1)(v_2 - u_2)}{2} + \frac{|\vec{u}||\vec{v}| \sin \theta}{2} \\

2 u_1 v_2 & = u_1 u_2 + v_1 v_2 + (u_1 - v_1)(v_2 - u_2) + |\vec{u}||\vec{v}| \sin \theta \\

2 u_1 v_2 & = \cancel{u_1 u_2} + \cancel{v_1 v_2} + u_1 v_2 - \cancel{u_1 u_2} - \cancel{v_1 v_2} + u_2 v_1 + |\vec{u}||\vec{v}| \sin \theta \\

u_1 v_2 - u_2 v_1 & = |\vec{u}||\vec{v}| \sin \theta
\end{aligned}
$$

I mean, come on! That is nice.

:::

This neat little formula is beautiful, and is used all over computer graphics.
But there's a punchline. Let $\vec{v}_{\perp}$ be the perpendicular to $\vec{v}$
(see [orthogonality](../vectors/orthogonality)):

$$
\vec{v}_{\perp} = \begin{bmatrix} v_2 \\ - v_1 \end{bmatrix}
$$

Now look at the formula for the area. Are you getting a certain creeping
feeling?

$$
\begin{aligned}
\text{Area}
& = u_1 v_2 - u_2 v_1 \\[5pt]
& = \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} \cdot \begin{bmatrix} v_2 \\ - v_1 \end{bmatrix} \\[5pt]
& = \vec{u} \cdot \vec{v}_{\perp}
\end{aligned}
$$

The god damn dot product again! We can't get away from the thing.

::: tip

The area of a parallelogram spanned by $\vec{u}$ and $\vec{v}$ in $2$ dimensions
can be given by

$$
u_1 v_2 - u_2 v_1
$$

This can be expressed in the form

$$
\vec{u} \cdot \vec{v}_{\perp}
$$

:::

## Code

As mentioned, we don't need to hardcode `u[0] * v[1] - v[0] * u[1]` directly, as
we can use `u @ v.perp()`. It has no computational benefit, really, but it looks
cool.

::: code-group

```py [vector.py]
@classmethod
def vol(cls, vectors: list[Vector]) -> float:
    dim = len(vectors)

    if any(v.dim != dim for v in vectors):
      raise ValueError("Require n vectors in n dimensions")

    if dim == 2:
      u, v = vectors
      return u @ v.perp()
```

:::

I've called this `vol` for _volume_ because we will soon generalise to higher
dimensions.
