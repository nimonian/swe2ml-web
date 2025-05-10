# Dot product properties

We can check a couple of important properties for the dot product.

## Scale factors

We can "factor out" scalars

$$
\left( \lambda\vec{u} \right) \cdot \left( \mu\vec{v} \right) = \lambda
\mu \left( \vec{u} \cdot \vec{v} \right)
$$

```py
def test_dot_product_properties():
    u = Vector([1, 3])
    v = Vector([4, 2])

    assert (2 * u) @ (3 * v) == 6 * (u @ v)
```

## Vector magnitude

Dotting a vector with itself gives the square of its magnitude

$$ \vec{u} \cdot \vec{u} = |\vec{u}|^2$$

If you take the time to write them out, both of these give

$$
u_1^2 + u_2^2 + \ldots + u_n^2
$$

so this should pass:

```py
assert u @ u == abs(u) ** 2
```

We could even refactor `Vector.__abs__` to make use of the dot product.

```py
def __abs__(self) -> float:
    return sqrt(sum(x**2 for x in self)) # [!code --]
    return sqrt(self @ self) # [!code ++]
```

## Perpendicular vectors

Two vectors have $0$ dot product if, and only if, they are perpendicular (at
$90^{\circ}$) to each other. This is because the $\cos \theta$ part of the dot
product is $0$ only when $\theta$ is a multiple of $90^{\circ}$.

$$
\vec{u} \cdot \vec{v} = 0 \quad \Leftrightarrow \quad \vec{u} \perp \vec{v}
$$

```py
assert u @ Vector([-3, 1]) == 0
```

::: info

Mathematics can't have just one name for things. Oh no. You may also see the
words **orthogonal** or **normal**. They are synonymous with **perpendicular**.

The word **normal** has the benefit that it can be used both as a noun and
adjective, so it has that going for it.

:::
