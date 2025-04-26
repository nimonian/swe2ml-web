# Linear transformations

So a matrix can transform a vector. Big wow. This still all seems pretty
arbitrary. I mean, I can transform a vector, too - you don't hear me bragging
about it. To understand what makes matrices special, we need to understand what
a **linear transformation** is. Come with me on a journey. Bring tea.

Remember [linear combinations](/learn/vectors/linear-combinations)? This means
taking two vectors, scaling them then adding them:

$$
\lambda \vec{u} + \mu \vec{v}
$$

Well, a **linear transformation** is a function `f(v: Vector) -> Vector`, with
the special property that whether you do the linear combination before or after,
you get the same result:

```python
assert f(2 * u + 3 * v) == 2 * f(u) + 3 * f(v)
```

Or, mathematically, a function $f$ is a linear transformation if

$$
f(\lambda \vec{u} + \mu \vec{v}) = \lambda f(\vec{u}) + \mu f(\vec{v})
$$

Why am I telling you all this? Well, it just so happens that multiplying a
vector by a matrix is a linear transformation:

$$
M(\lambda \vec{u} + \mu \vec{v}) = \lambda M \vec{u} + \mu M \vec{v}
$$

But wait a minute, that isn't the best part. There is a much, much deeper
statement we can make: **every linear transformation is a matrix**. Now this
sounds truly insane. The ramblings of a madman. Just why in the hell should this
be the case? Matrices are just big dumb tables, linear transformations seem much
more general than that.

But here we are. It's true.

::: tip

Any linear transformation $f$ can be represented by some matrix $M$. This means
that we can always find a matrix such that:

$$
f(\vec{v}) = M\vec{v}
$$

The columns of $M$ are the vectors produced when $f$ acts on the basis vectors
$\hat{i}, \hat{j}, \ldots$.

:::

::: details

To save us from notation hell, I'm just going to prove this for a function from
$2$ dimensions to $2$ dimensions. The proof generalises to any combination of
dimensions very easily.

Suppose

$$
\vec{v} = \begin{bmatrix} x \\ y \end{bmatrix} \quad
\hat{i} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \quad
\hat{j} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

and let

$$
f(\hat{i}) = \begin{bmatrix} a \\ c \end{bmatrix} \quad f(\hat{j}) = \begin{bmatrix} b \\ d \end{bmatrix}
$$

Then, if $f$ is linear,

$$
\begin{aligned}
f(\vec{v})
& = f(x \hat{i} + y \hat{j}) \\
& = x f(\hat{i}) + y f (\hat{j}) && \text{(because linear)} \\
& = x \begin{bmatrix} a \\ c \end{bmatrix} + y \begin{bmatrix} b \\ d \end{bmatrix} \\
& = \begin{bmatrix} ax + by \\ cx + dy \end{bmatrix} \\
& = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix}
\end{aligned}
$$

:::

Although linear transformations are important objects, there is no point making
a `LinearTransform` class, because that is literally just the `Matrix` class.
