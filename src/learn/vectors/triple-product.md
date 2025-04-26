# Triple product

The magnitude of the [cross product](../vectors/cross-product-3d.md) gives us
the area of the parallelogram determined by two vectors. If we're given three
vectors, however, they determine a **parallelepiped**.

![](../../images/parallelepiped.svg)

A parallelepiped is a bit like a wonky cube. We're interested to find the
**volume** of this shape. Let's label a few things on our picture.

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

This is known as the **triple product** of the vectors.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_triple_product

<<< @/../pycode/models/vector.py#vector_triple_product

:::

Writing out the vector components, we get

$$
\begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix}
\cdot
\begin{bmatrix} v_2 w_3 - v_3 w_2 \\ v_3 w_1 - v_1 w_3 \\ v_1 w_2 - v_2 w_1 \end{bmatrix}
$$

It turns out that if we "rotate" the position of the vectors in this formula, we
still get the exact same volume:

$$
\vec{u} \cdot (\vec{v} \times \vec{w})
= \vec{w} \cdot (\vec{u} \times \vec{v})
= \vec{v} \cdot (\vec{w} \times \vec{u})
$$

<<< @/../pycode/models/vector_test.py#test_vector_triple_product_2

However, if we "flip" the position of two vectors, we get the negative of the
volume:

$$
\vec{v} \cdot (\vec{u} \times \vec{w}) = - \vec{u} \cdot (\vec{v} \times \vec{w})
$$

If we just want the geometric volume as a positive number, we should not care
about the order of the vectors, and take the magnitude of the triple product.

## Exercise

<Exercise id="triple-product" />
