# Generalised cross product

We have seen in [](../vectors/orthogonality) how to find $\vec{u}_{\perp}$ which
is normal to a single vector in $2$ dimensions. We've also seen how to find
$\vec{u} \times \vec{v}$, a vector normal to $\vec{u}$ and $\vec{v}$ in three
dimensions.

The question becomes, if we're given $n$ vectors in $(n + 1)$ dimensional space,
can we find another vector

$$
\vec{n} = \vec{v}_1 \times \vec{v}_2 \times \ldots \times \vec{v}_{n}
$$

which is normal to all of them? The answer is yes. But it gets weird.

Look at

$$
\vec{u} \times \vec{v} =
\begin{bmatrix}
u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1
\end{bmatrix}
$$

The components are [areas of parallelograms](./parallelograms). In fact, they
are found by omitting the first, second, and third components of $\vec{u}$ and
$\vec{v}$ respectively.

$$
\vec{u} \times \vec{v} =

\begin{bmatrix}

\text{vol} \left(
\begin{bmatrix}
u_2 \\ u_3
\end{bmatrix},
\begin{bmatrix}
v_2 \\ v_3
\end{bmatrix}
\right) \\

- \text{vol} \left(
\begin{bmatrix}
u_1 \\ u_3
\end{bmatrix},
\begin{bmatrix}
v_1 \\ v_3
\end{bmatrix}
\right) \\

\text{vol} \left(
\begin{bmatrix}
u_1 \\ u_2
\end{bmatrix},
\begin{bmatrix}
v_1 \\ v_2
\end{bmatrix}
\right)

\end{bmatrix}
$$

Following this pattern gives us a way to compute the normal to any number of
vectors. If we let $V_{i}$ be the volume formed by the vectors with the
$i^{\text{th}}$ component ommited, then

$$
\vec{v}_1 \times \vec{v}_2 \times \ldots \times \vec{v}_{n}
=
\begin{bmatrix}
V_1 \\ -V_2 \\ V_3 \\ -V_4 \\ \vdots \\ \pm V_n
\end{bmatrix}
$$

## Code

::: code-group

```py [vector.py]
def omit(self, i):
    return Vector(self.components[:i] + self.components[i + 1:])

@classmethod
def cross(cls, vectors: Sequence[Vector]) -> Vector:
    dim = len(vectors) + 1

    if any(v.dim != dim for v in vectors):
        raise ValueError("Requires n vectors in (n + 1)-dimensional space")

    if dim == 3:  # [!code --:12]
        u, v = vectors

        return Vector(
            [
                u[1] * v[2] - u[2] * v[1],
                u[2] * v[0] - u[0] * v[2],
                u[0] * v[1] - u[1] * v[0],
            ]
        )

    raise NotImplementedError

    return Vector( # [!code ++:4]
      (-1)**i * cls.vol(v.omit(i))
      for i, v in enumerate(vectors)
    )
```

:::
