"""Example tests that showcases asynctest functionalities."""
import asyncio
import asynctest
import datetime


class ExampleTestCase(asynctest.TestCase):
    """Test case that includes asyncio examples."""

    def print_something(self) -> None:
        """Print something."""
        print("Something!")

    async def test_string_append(self):
        """Test string append."""
        self.assertEqual('abc', 'a' + 'b' + 'c')

    async def test_make_request(self):
        """Test some async functionalty.

        In this case, we test that `asyncio.sleep` delays the right
        amount of time.
        """
        delay = 1
        before = datetime.datetime.now()
        # Get event loop using `self.loop`
        self.loop.call_later(delay / 2, self.print_something)
        await asyncio.sleep(delay)
        after = datetime.datetime.now()
        self.assertTrue(after - before > datetime.timedelta(seconds=delay))


if __name__ == '__main__':
    asynctest.main()
