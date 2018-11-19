"""Module defines custom types that leverages type annotations.

Type annotations were implemented in Python 3.6 and allow for static
time type checking.
"""
from typing import Generic, TypeVar

T = TypeVar('T')


class Pair(Generic[T]):
    """Type that defines a pair of values of type `T`."""

    def __init__(self, a: T, b: T):
        """Initialize the `Pair` class.

        Args:
            a: the first argument.
            b: the second argument.
        """
        self.a = a
        self.b = b

    def __getitem__(self, index: int) -> T:
        """Get the item of type `T` at `index`."""
        if index == 0:
            return self.a
        if index == 1:
            return self.b

        raise IndexError(index)

    def __setitem__(self, index: int, value: T) -> None:
        """Set the item of type `T` at `index`."""
        if index == 0:
            self.a = value
        elif index == 1:
            self.b = value

        raise IndexError(index)

    def __str__(self) -> str:
        """Stringify the object."""
        return f'Pair({self.a}, {self.b})'


if __name__ == '__main__':
    pair_of_int: Pair[int] = Pair(1, 2)  # Type annotation on assignment.
    print(pair_of_int)

    pair_of_pair: Pair[Pair[int]] = Pair(Pair(1, 2), Pair(1, 2))
    print(pair_of_pair)

    check_failed_pair: Pair[int] = Pair('1', 2)  # Static type check fails here
