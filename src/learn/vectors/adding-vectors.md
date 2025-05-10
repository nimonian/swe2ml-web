# Adding vectors

On the previous page, we said vectors do more than just coordinates, and then we
implemented a `Vector` class that is basically just a coordinate class. Let's
add a bit more behaviour to justify our grand claims.

We add two vectors by just adding their components to make a new vector. For
example,

$$
\begin{bmatrix}
3 \\ 1
\end{bmatrix}
+
\begin{bmatrix}
1 \\ 2
\end{bmatrix}
=
\begin{bmatrix}
4 \\ 3
\end{bmatrix}
$$

Generally,

$$
\begin{bmatrix}
u_1 \\ u_2 \\ \vdots \\ u_n
\end{bmatrix}
+
\begin{bmatrix}
v_1 \\ v_2 \\ \vdots \\ v_n
\end{bmatrix}
=
\begin{bmatrix}
u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n
\end{bmatrix}
$$

We can interpret vector addition in a visual way. If

$$
\vec{u} = \begin{bmatrix} 3 \\ 1 \end{bmatrix} \quad \vec{v} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}
$$

Then adding $\vec{v}$ to $\vec{u}$ means placing the base of $\vec{v}$ at the
tip of $\vec{u}$. We just glue the vectors together in the dumbest way possible
to make the new vector $\vec{u} + \vec{v}$.

![](/images/vector-addition.svg)

Try counting the squares to make sure this makes sense to you. Notice also that
the order in which we add the vectors doesn't affect the output.

![](/images/vector-addition-2.svg)

In other words,

$$
\vec{u} + \vec{v} = \vec{v} + \vec{u}
$$

I sometimes say that, if points are like a specific times of the day, then
vectors are more like **durations**. We can't add times, but we can add
durations to get new durations.

## Code

To implement vector addition in our `Vector` class, we can override the `+`
operator by defining an `__add__` method.

::: code-group

<<< @/../pycode/models/vector_test.py#test_vector_addition

<<< @/../pycode/models/vector.py#vector_addition

:::

## Exercise

<Exercise id="adding-vectors" />
