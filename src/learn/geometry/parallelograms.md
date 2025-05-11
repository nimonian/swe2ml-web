# Parallelograms

Given two vectors, we can create a parallelogram like this:

![](../../images/vector-parallelogram.svg)

The area of the parallelogram can be found, through elementary geometry, to be

$$
|\vec{u}| |\vec{v}| \sin \theta
$$

I still can't find my protractor. Fortunately, I don't need it, because this
area can be expressed purely in terms of the components of the vectors! It is

$$
\text{vol}\left( \vec{u}, \vec{v} \right) = u_1 v_2 - u_2 v_1
$$

::: details

Check this picture out:

![](../../images/cross-prod-proof.svg)

The area of the middle triangle is found by subtracting the three coloured
triangles from the surrounding rectangle:

$$
u_1v_1 - \frac{u_1 u_2}{2} - \frac{v_1 v_2}{2} - \frac{(u_1 - v_1)(v_2 - u_2)}{2}
$$

If we expand and simplify we get

$$
\frac{1}{2} \left(2 u_1 v_1 - \cancel{u_1 u_2} - \cancel{v_1 v_2} - u_1 v_2 + \cancel{u_1 u_2} + \cancel{v_1 v_2} - u_2 v_1 \right)
$$

or

$$
\frac{1}{2} \left( u_1 v_2 - u_2 v_1 \right)
$$

The triangle is half the parallelogram, and so losing the $\frac{1}{2}$ from the
above gets us the area of the whole parallelogram.

:::

This neat little formula is beautiful, and is used all over the place. For
example, computer graphics relies on this to deal with all the polygons which
make up various shapes.

::: tip

The area of a parallelogram spanned by $\vec{u}$ and $\vec{v}$ in $2$ dimensions
can be given by

$$
\text{vol}\left( \vec{u}, \vec{v} \right) = u_1 v_2 - u_2 v_1
$$

:::

## Code

Now we can add the $2$-dimensional case to our `vol` function.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vol_2d

```py [vector.py]
@classmethod
def vol(cls, vectors: Iterable[Vector]) -> float:
    vectors = len(vectors)
    dim = len(vectors)

    if any(v.dim != dim for v in vectors):
        raise ValueError("Require n vectors in n dimensions")

    if dim == 1:
        [u] = vectors
        return u[0]

    if dim == 2: # [!code ++:3]
        u, v = vectors
        return u[0] * v[1] - u[1] * v[0]
```

:::
