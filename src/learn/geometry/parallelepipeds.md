# Parallelepipeds

We've seen how to find the area of a parallelogram given by two vectors. If
we're given three vectors, however, they determine a **parallelepiped**.

![](../../images/parallelepiped.svg)

A parallelepiped is a bit like a wonky cube. The volume is given by the formula

$$
\text{vol}\left( \vec{u}, \vec{v}, \vec{w} \right)
=
u_1 (v_2 w_3 - v_3 w_2) - u_2 (v_1 w_2 - v_3 w_1) + u_3 (v_1 w_2 - v_2 w_1)
$$

If it's ok with you, I'm going to delay the proof until after we study normal
vectors, because they simplify the problem of working out the _height_ of the
parallelepiped.

You might notice a few things about this formula. Keep reading!

## Code

Our function is getting smelly. That bit of my brain that wants to refactor is
tingling. Is there some further structure to exploit? Is there a pattern
developing? _Keep reading!_

::: code-group

<<< @/../pycode/models/vector_test.py#test_vol_3d

```py [vector.py]
@classmethod
def vol(cls, vectors: Iterable[Vector]) -> float:
    vectors = list(vectors)
    dim = len(vectors)

    if any(v.dim != dim for v in vectors):
        raise ValueError("Require n vectors in n dimensions")

    if dim == 1:
        [u] = vectors
        return u[0]

    if dim == 2:
        u, v = vectors
        return u[0] * v[1] - u[1] * v[0]

    if dim == 3: # [!code ++:7]
        u, v, w = vectors
        return (
          u[0] * (v[1] * w[2] - v[2] * w[1])
          - u[1] * (v[0] * w[2] - v[2] * w[1])
          + u[2] * (v[0] * w[1] - v[1] * w[0])
        )
```

:::
