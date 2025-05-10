# Magnitude revisited

Whoever said "If it isn't broken, don't fix it" has never experienced the
satisfaction of a truly clever refactor.

Our formula for magnitude

$$
|\vec{v}| = \sqrt{v_1^2 + v_2^2 + \ldots + v_n^2}
$$

comes out of Pythagoras' Theorem. Fine.

But look what happens, just **look what happens**, when you take the dot product
of a vector with itself:

$$
\begin{aligned}
\vec{v} \cdot \vec{v}
& = v_1 v_1 + v_2 v_2 + \ldots + v_n v_n \\
& = v_1^2 + v_2^2 + \ldots + v_n^2
\end{aligned}
$$

It's the same as the goddamn **magnitude**! Almost. It's missing the square
root. But it does allow us to write

$$
|\vec{v}|^2 = \vec{v} \cdot \vec{v}
$$

## Code

This is it. Our big moment. Behold:

```py
def __abs__(self) -> float:
    return sqrt(sum(x**2 for x in self)) # [!code --]
    return sqrt(self @ self) # [!code ++]
```

Fuck. Yes.
