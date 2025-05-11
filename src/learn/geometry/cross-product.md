# Cross product

If we have two vectors in $3$ dimensions, their **cross product**
$\vec{v} \times \vec{w}$ gives a third vector $\vec{n}$ which is
[perpendicular](../vectors/orthogonality) to both $\vec{v}$ and $\vec{w}$.

![](../../images/cross-prod-normal.svg)

Generally,
$\vec{n} = \vec{v}_1 \times \vec{v}_2 \times \ldots \times \vec{v}_{n-1}$ should
be another vector which is perpendicular to all the inputs. That is, we want

$$
\begin{aligned}
\vec{n} \cdot \vec{v}_1 & = 0 \\
\vec{n} \cdot \vec{v}_2 & = 0 \\
& \vdots \\
\vec{n} \cdot \vec{v}_{n-1} & = 0
\end{aligned}
$$

Our volume formula can help here:

$$
\text{vol}\left( \vec{u}, \,\, \vec{v}_1, \,\, \ldots, \,\, \vec{v}_{n-1} \right) = u_1 V_1 - u_2 V_2 + \ldots \pm u_n V_n
$$

If we let

$$
\vec{n} = \begin{bmatrix} V_1 \\ - V_2 \\ \vdots \\ \pm V_n \end{bmatrix}
$$

then we can write the volume as

$$
\text{vol}\left( \vec{u}, \,\, \vec{v}_1, \,\, \ldots, \,\, \vec{v}_{n-1} \right) = \vec{u} \cdot \vec{n}
$$

Is it clear why the volume $\vec{v}_i \cdot \vec{n}$ must be $0$? If two of the
vectors forming the parallelotope are equal, then it has no "height" in $n$
dimensions, and therefore no volume.

In $3$ dimensions, we get

$$
\vec{n} = \vec{v} \times \vec{w} = \begin{bmatrix} v_2 w_3 - v_3 w_2 \\ v_3 w_1 - v_1 w_2 \\ v_1 w_2 - v_2 w_1 \end{bmatrix}
$$

## Code

Let's get this into our class before my head explodes.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_cross_product

<<< @/../pycode/models/vector.py#vector_cross_product

:::

Because

$$
\text{vol}\left( \vec{u}, \,\, \vec{v}_1, \,\, \ldots, \,\, \vec{v}_{n-1} \right) = \vec{u} \cdot \left( \vec{v}_1 \times \vec{v}_2 \times \ldots \times \vec{v}_{n-1} \right)
$$

we can refactor `vol` to use `cross`

```py
@classmethod
def vol(cls, vectors: Iterable[Vector]) -> float:
    vectors = tuple(vectors)
    dim = len(vectors)

    if any(v.dim != dim for v in vectors):
        raise ValueError("Require n vectors in n dimensions")

    if dim == 1:
        [u] = vectors
        return u[0]

    u, *rest = vectors

    return u @ cls.cross(rest) # [!code ++]

    V = [Vector.vol(v.omit(i) for v in vectors) for i in range(dim)] # [!code --]
    return sum((-1) ** i * u[i] * V[i] for i in range(dim)) # [!code --]
```

## Exercise

<Exercise id="cross-product" />
