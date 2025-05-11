# Triple product

There's a mathematically pleasant way of expressing the volume of a
parallelotope:

$$
\text{vol}\left( \vec{u}, \,\, \vec{v}_1, \,\, \ldots, \,\, \vec{v}_{n-1} \right) = \vec{u} \cdot \left( \vec{v}_1 \times \vec{v}_2 \times \ldots \times \vec{v}_{n-1} \right)
$$

::: details

$$
\begin{aligned}
\text{vol}\left( \vec{u}, \,\, \vec{v}_1, \,\, \ldots, \,\, \vec{v}_{n-1} \right)
& = u_1 V_1 - u_2 V_2 + \ldots \pm u_n V_n \\[5pt]
& = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{bmatrix} \cdot \begin{bmatrix} V_1 \\ - V_2 \\ \vdots \\ \pm V_n \end{bmatrix} \\[5pt]
& = \vec{u} \cdot \left( \vec{v}_1 \times \vec{v}_2 \times \ldots \times \vec{v}_{n-1} \right)
\end{aligned}
$$

:::

::: details

Let's label a few things on our picture.

![](../../images/parallelepiped-2.svg)

The vector $\vec{v} \times \vec{w}$ is perpendicular to $\vec{v}$ and $\vec{w}$.
The height of the parallelepiped is therefore $|\vec{u}|\cos\varphi$, and the
volume is

$$
\begin{aligned}
\text{Volume} & = \text{Area of base} \times \text{height} \\
& = |\vec{v}||\vec{w}|\sin\theta \times |\vec{u}|\cos\varphi \\
& = |\vec{v} \times \vec{w}| |\vec{u} | \cos \varphi \\
& = \vec{u} \cdot (\vec{v} \times \vec{w})
\end{aligned}
$$

Here, we have used that

$$
|\vec{v} \times \vec{w}| = |\vec{v}||\vec{w}|\sin\theta
$$

which is explained [here](./cross-product-area).

:::

This is known as the **triple product** of the vectors.

## Code

With this, we're able to generalise our `vol` method a bit further!

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_triple_product

```py [vector.py]
def vol(cls, vectors: list[Vector]) -> float:
    dim = len(vectors)

    if any(v.dim != dim for v in vectors):
        raise ValueError("Require n vectors in n dimensions")

    if dim == 2:
        u, v = vectors
        return u @ v.perp()

    if dim == 3: # [!code ++:3]
        u, v, w = vectors
        return u @ Vector.cross([u, v])
```

:::

## Exercise

<Exercise id="triple-product" />
