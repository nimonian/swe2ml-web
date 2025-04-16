# Vector magnitude

Some vectors are big; some vectors are small. That's ok. But for the good of
science we'd like to assign a number to measure the size.

To do this, we might remember a little fact about triangles known as Pythagoras'
theorem.

![](../../images/pythagoras.svg)

The fact is that

$$
z = \sqrt{x^2 + y^2}
$$

If you have never seen a proof, my personal favourite is given below.

::: details

![](../../images/pythag-proof.svg)

The area of the above image can be found in two ways.

First, by summing the area of the four triangles plus the square in the middle:

$$
\begin{aligned}
& z^2 + 4 \times \frac{xy}{2} \\
= {} & z^2 + 2xy
\end{aligned}
$$

Second, by multiplying the overall height by the overall width:

$$
\begin{aligned}
& (x + y)^2 \\
= {} & x^2 + y^2 + 2xy
\end{aligned}
$$

As these expressions both equal the area, they must equal each other, and so

$$
\begin{aligned}
z^2 + 2xy & = x^2 + y^2 + 2xy \\
z^2 & = x^2 + y^2
\end{aligned}
$$

:::

We denote the magnitude (that is to say, the length) of $\vec{v}$ by
$|\vec{v}|$. So just how long is the vector

$$
\vec{v} = \begin{bmatrix} 4 \\ 3 \end{bmatrix}?
$$

Let's draw the thing

![](../../images/vector-magnitude.svg)

Now, we see very clearly by Pythagoras' theorem that

$$
\begin{aligned}
|\vec{v}|
& = \sqrt{4^2 + 3^2} \\
& = \sqrt{25} \\
& = 5 \\
\end{aligned}
$$

Generally, we define

$$
|\vec{v}| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
$$

Let's implement this in our `Vector` class. We'll override the `abs()` function
because `abs` stands for "absolute value", which basically means the size,
irrespective of direction. Just in the same way that `abs(-2)` gives `2`,
calling `abs(v)` should give the size of the thing.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_magnitude

<<< @/../pycode/models/vector.py#vector_magnitude

:::

We said [scalar multiplication](./scaling-vectors) stretches a vector. This
basically means that $\lambda \vec{v}$ is $\lambda$ times longer than $\vec{v}$.
Now we have a mathematical formula for the length, we're in a position to prove
this.

I'm going to put the proof in a dropdown so you know it's optional, but if you
are in any way dubious of my claims about stretching vectors, you should give it
a read.

::: details

In words: the length of the vector $\lambda \vec{v}$ is $\lambda$ times the
length of $\vec{v}$.

In symbols: $|\lambda \vec{v}| = \lambda |\vec{v}|$.

The proof:

$$
\begin{aligned}
|\lambda\vec{v}|
& = \sqrt{(\lambda v_1)^2 + (\lambda v_2)^2 + \ldots + (\lambda v_n)^2} \\
& = \sqrt{\lambda^2 v_1^2 + \lambda^2 v_2^2 + \ldots + \lambda^2 v_n^2} \\
& = \sqrt{\lambda^2(v_1^2 + v_2^2 + \ldots + v_n^2)} \\
& = \sqrt{\lambda^2} \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2} \\
& = \lambda \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2} \\
& = \lambda |\vec{v}|
\end{aligned}
$$

:::

## Exercise

<Exercise id="vector-magnitude" />

After doing this exercise a few times, you might start to notice that
$|\vec{v}|$ is always positive (or $0$). In fact, it's only $0$ if all the
components are themselves $0$. This all seems clear when you think about
squaring numbers and adding the results.
