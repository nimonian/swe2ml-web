# Dot product formula

Even if you believe me that this $|\vec{u}| |\vec{v}| \cos \theta$ number is
useful, who on earth has time for measuring the angle between two vectors? I
don't even own a protractor. Good job there's a trick, which I will prove in the
box below, that simplifies calculating the dot product immensely.

::: details

I'll do it for $2$ dimensions - the only difficulty in generalising is fiddling
with notation.

![](../../images/dot-prod-proof.svg)

By subtracting the vectors and taking the magnitude, we see that

$$
\begin{aligned}
|\vec{v} - \vec{u}|^2
& = (v_1 - u_1)^2 + (v_2 - u_2)^2 \\
& = v_1^2 + u_1^2 - 2u_1v_1 + v_2^2 + u_2^2 - 2u_2v_2 \\
& = (u_1^2 + u_2^2) + (v_1^2 + v_2^2) - 2u_1v_1 - 2u_2v_2 \\
& = |\vec{u}|^2 + |\vec{v}|^2 - 2(u_1v_1 + u_2v_2)
\end{aligned}
$$

On the other hand, we have from the
[cosine rule](https://mathematico.netlify.app/pure/trigonometry/cos-rule/) that

$$
|\vec{v} - \vec{u}|^2 = |\vec{u}|^2 + |\vec{v}|^2 - 2|\vec{u}||\vec{v}| \cos \theta
$$

Both of these results equal $|\vec{v} - \vec{u}|^2$, and therefore they must be
equal to each other:

$$
\begin{aligned}
\cancel{|\vec{u}|^2} + \cancel{|\vec{v}|^2} - 2|\vec{u}||\vec{v}| \cos \theta & = \cancel{|\vec{u}|^2} + \cancel{|\vec{v}|^2} - 2(u_1v_1 + u_2v_2) \\
\cancel{- 2}|\vec{u}||\vec{v}| \cos \theta & = \cancel{- 2}(u_1v_1 + u_2v_2) \\
|\vec{u}||\vec{v}| \cos \theta & = u_1v_1 + u_2v_2 \\
\end{aligned}
$$

And holy shit if that isn't our dot product on the left side of the equation.

:::

Hilariously, it turns out that the dot product is the sum of the components of
the Hadamard product:

$$
\vec{u} \cdot \vec{v} = u_1 v_1 + u_2 v_2 + \ldots + u_n v_n
$$

Now we can very easily compute, for example,

$$
\begin{aligned}
\begin{bmatrix} 1 \\ 3 \end{bmatrix} \cdot \begin{bmatrix} 4 \\ 2 \end{bmatrix}
& = 1 \times 4 + 3 \times 2 \\
& = 4 + 6 \\
& = 10
\end{aligned}
$$

This is _wonderful_, because it means we can compute $\vec{u} \cdot \vec{v}$
without even knowing the value of $\theta$.

When it comes to our `Vector` class, Python has the `@` infix which is
[intended to be used](https://peps.python.org/pep-0465/) for the dot product. To
implement it, we define the `__matmul__` dunder method.

::: code-group

<<< @/../pycode/models/vector_test.py#test_dot_product

<<< @/../pycode/models/vector.py#dot_product

:::

We can also check a couple of important properties for the dot product.

1. We can "factor out" scalars

   $$
   \left( \lambda\vec{u} \right) \cdot \left( \mu\vec{v} \right) = \lambda
   \mu \left( \vec{u} \cdot \vec{v} \right)
   $$

2. Dotting a vector with itself gives the square of its magnitude

   $$ \vec{u} \cdot \vec{u} = |\vec{u}|^2 $$

3. Two vectors have $0$ dot product if, and only if, they are perpendicular (at
   $90^{\circ}$) to each other

   $$
   \vec{u} \cdot \vec{v} = 0 \quad \Leftrightarrow \quad \vec{u} \perp \vec{v}
   $$

<<< @/../pycode/models/vector_test.py#test_dot_product_2

There's no work to do in `Vector` - this is all guaranteed by the definition of
the dot product.

## Exercise

<Exercise id="dot-product-formula" />
