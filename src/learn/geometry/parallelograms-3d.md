# $3$ dimensions

If the vectors are $3$-dimensional, we can visualise the parallelogram floating
in space.

![](../../images/plane-3d.svg)

The area formula becomes

$$
\text{Area} = \sqrt{(u_2 v_3 - u_3 v_2)^2 + (u_3 v_1 - u_1 v_3)^2 + (u_1 v_2 - u_2 v_1)^2}
$$

::: details

Get ready...

$$

\begin{aligned}
\text{Area}^2
& = |\vec{u}|^2 |\vec{v}|^2 - \left(\vec{u} \cdot \vec{v} \right)^2 \\

& = \left( u_1^2 + u_2^2 + u_3^2
\right)\left( v_1^2 + v_2^2 + v_3^2 \right) - \left( u_1v_1 + u_2v_2 + u_3v_3
\right)^2 \\

& = \cancel{u_1^2 v_1^2} + u_1^2 v_2^2 + u_1^2 v_3^2 + u_2^2
v_1^2 + \cancel{u_2^2 v_2^2} + u_2^2 v_3^2 + u_3^2 v_1^2 + u_3^2 v_2^2 +
\cancel{u_3^2 v_3^2} \\

& \quad - \cancel{u_1^2 v_1^2} - \cancel{u_2^2 v_2^2} -
\cancel{u_3^2 v_3^2} - 2\left( u_2v_2u_3v_3 + u_3v_3u_1v_1 + u_1v_1u_2v_2
\right) \\ & = u_2^2 v_3^2 + u_3^2 v_2^2 - 2 u_2 v_2 u_3 v_3 + u_3^2 v_1^2 +
u_1^2 v_3^2 - 2 u_3 v_3 u_1 v_1 + u_1^2 v_2^2 + u_2^2 v_1^2 - 2 u_1v_1u_2v_2 \\

& = (u_2 v_3 - u_3 v_2)^2 + (u_3 v_1 - u_1 v_3)^2 + (u_1 v_2 - u_2 v_1)^2 \\

& = | \vec{u} \times \vec{v} |^2
\end{aligned}
$$

Phew!

:::

Remember the cross product?

$$
\vec{u} \times \vec{v} = \begin{bmatrix}
u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1
\end{bmatrix}
$$

Well, look at the area of the parallelogram we just found above. Yep, it's the
magnitude of $\vec{u} \times \vec{v}$.

$$
\text{Area} = | \vec{u} \times \vec{v} |
$$
