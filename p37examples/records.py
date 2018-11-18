"""Python 3.7 dataclass example.

Dataclasses are classes that implement very few (public) methods
and are instead used for instantiating objects with specific attributes
this is particularly common in ORM(Object relation mapping).

Python 3.7 includes the `dataclasses` module with the `dataclass`
decorator that removes some of the pains of creating a dataclass.
"""
from dataclasses import InitVar, dataclass, make_dataclass
from functools import wraps


class VersionError(Exception):
    """Error raised when version is incorrect."""

    pass


class MinorVersionError(VersionError):
    """Error raised when minor version is incorrect."""

    def __init__(self, minor: int):
        """Initialize `MinorVersionError`.

        Args:
            minor: The minor version supplied.
        """
        super().__init__(f"Unexpected minor version {minor}")


def version(minor: int):
    """Decorate the VersionRecord with the expected minor version.

    Args:
        minor: The minor version number.
    """
    def _decorator(cls):
        @wraps(cls)
        def _wraps(_minor: int, **kwargs):
            if _minor > minor:
                raise MinorVersionError(_minor)
            elif _minor < minor:
                upgrade_fn_name = f'upgrade_{_minor}_{minor}'
                if not hasattr(cls, upgrade_fn_name):
                    raise MinorVersionError(_minor)
                kwargs = getattr(cls, upgrade_fn_name)(kwargs)
            obj = cls(_minor, **kwargs)
            return obj
        return _wraps
    return _decorator


@dataclass
class VersionedRecord:
    """The version record base class.

    Sub-clases should be the form of `{class_name}_v{major_version}`.
    """

    _minor: int

    @property
    def minor(self) -> int:
        """Get the minor version."""
        return self._minor

    @property
    def major(self) -> int:
        """Get the major version."""
        try:
            return int(self.__class__.__name__.split('_v')[-1])
        except IndexError:
            raise VersionError("Unable to parse major version number")

    @property
    def version(self) -> str:
        """Get the full version."""
        return f'{self.major}.{self.minor}'


@version(minor=1)
@dataclass
class FeedKey_v0(VersionedRecord):
    """The version record containing the feed_key."""

    feed_key: str


if __name__ == '__main__':
    fk = FeedKey_v0(1, feed_key='FEED_KEY')
    print(repr(fk))
