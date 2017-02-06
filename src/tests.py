import unittest

import basin


class Test(unittest.TestCase):

    def test_encode(self):
        self.assertEqual("a", basin.encode("abc", 0))
        self.assertEqual("ba", basin.encode("abc", 3))

    def test_decode(self):
        self.assertEqual(0, basin.decode("abc", "a"))
        self.assertEqual(3, basin.decode("abc", "ba"))


