# Subtracting vectors

Here's how I wish it was explained to me:

- How do you get from $7$ to $10$? The answer is $10 - 7 = 3$.
- How do you get from $5$ to $1$? The answer is $1 - 5 = -4$.
- How do you get from the tip of $\vec{u}$ to the tip of $\vec{v}$? The answer
  is $\vec{v} - \vec{u}$.

The picture also helps a lot.

![](/images/vector-subtraction.svg)

If we count the squares, we see that

$$
\begin{aligned}
\vec{v} - \vec{u}
& = \begin{bmatrix} 2 \\ 3 \end{bmatrix} - \begin{bmatrix} 4 \\ 1 \end{bmatrix} \\
& = \begin{bmatrix} 2 - 4 \\ 3 - 1 \end{bmatrix} \\
& = \begin{bmatrix} -2 \\ 2 \end{bmatrix}
\end{aligned}
$$

Let's get this into our `Vector` class:

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_subtraction

<<< @/../pycode/models/vector.py#vector_subtraction

:::

This implementation is clever, isn't it? Mathematics enjoys this efficiency,
too. We like to say that $\vec{v} - \vec{u} = \vec{v} + (-\vec{u})$ to avoid
defining a new operation called "subtraction" - it seems wasteful when we can
just combine addition with scalar multiplication.

In combination with vector magnitude, vector subtraction is particularly useful,
since

$$
|\vec{v} - \vec{u}|
$$

represents the distance from $\vec{u}$ to $\vec{v}$.

## Exercise

<Exercise id="subtracting-vectors" />
