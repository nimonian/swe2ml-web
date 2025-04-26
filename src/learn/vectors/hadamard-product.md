# The Hadamard product

Adding two vectors is pretty natural, but when it comes to multplying two
vectors, things get tribal: there is a lot of competition for the title of
"product of two vectors".

The most obvious product between two vectors is defined component-wise, just
like addition:

$$
\begin{bmatrix} 3 \\ 2 \end{bmatrix} \odot \begin{bmatrix} 2 \\ 4 \end{bmatrix}
= \begin{bmatrix} 3 \times 2 \\ 2 \times 4 \end{bmatrix}
= \begin{bmatrix} 6 \\ 8 \end{bmatrix}
$$

In general,

$$
\vec{u} \odot \vec{v}
= \begin{bmatrix} u_1 v_1 \\ u_2 v_2 \\ \vdots \\ u_n v_n \end{bmatrix}
$$

Given how natural this product feels, why the fancy name and $\odot$ symbol? The
fact is that, for mathematics, it's just not paricularly interesting: it doesn't
encapsulate much meaning or structure about vectors. It's so mathematically
boring that there aren't even any pictures on this page as there's nothing to
draw.

For computational purposes, though, it sure is convenient! So in our code, we'll
bestow upon it the honour of the `*` operator, even if it means refactoring
`__mul__`:

::: code-group

<<< @/../pycode/models/vector_test.py#test_hadamard_product

<<< @/../pycode/models/vector.py#vector_hadamard_product

:::

## Exercise

<Exercise id="hadamard-product" />
