# Parallelograms

Given two vectors, we can create a parallelogram like this:

![](../../images/vector-parallelogram.svg)

The area of the parallelogram can be found, through elementary geometry, to be

$$
\text{Area} = |\vec{u}| |\vec{v}| \sin \theta
$$

I still can't find my protractor. Fortunately, I don't need it, because this
area can be expressed purely in terms of the components of the vectors! It is

$$
\text{Area} = \sqrt{ |\vec{u}|^2 |\vec{v}|^2 - (\vec{u} \cdot \vec{v})^2}
$$

::: details

Remembering that $\sin^2 \theta = 1 - \cos^2 \theta$, we find that

$$
\begin{aligned}
\text{Area}^2 & = |\vec{u}|^2 |\vec{v}|^2 \sin^2 \theta \\
& = |\vec{u}|^2 |\vec{v}|^2 \left(1 - \cos^2 \theta \right) \\
& = |\vec{u}|^2 |\vec{v}|^2 - \left( |\vec{u}||\vec{v}|\cos \theta \right)^2 \\
& = |\vec{u}|^2 |\vec{v}|^2 - \left(\vec{u} \cdot \vec{v} \right)^2 \\
\end{aligned}
$$

:::

::: tip

[Recall](../vectors/dot-prod-properties#vector-magnitude) that
$|\vec{u}|^2 = \vec{u} \cdot \vec{u}$. The above formula is more convenient to
compute as

$$
\text{Area} = \sqrt{ (\vec{u} \cdot \vec{u})(\vec{v} \cdot \vec{v}) - (\vec{u} \cdot \vec{v})^2}
$$

:::

The special cases in $2$ and $3$ dimensions deserve a bit of attention.

## Code

The code for this formula basically writes itself, because we have already
implemented the algebra required to express it.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_area

<<< @/../pycode/models/vector.py#vector_area

:::

## Exercise

<Exercise id="parallelograms" />
