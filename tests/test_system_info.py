import unittest
from jml_tcr import get_threads


class MyTestCase(unittest.TestCase):
    def test_get_threads(self):
        # self.assertEqual(True, False)  # add assertion here
        dict_thr = get_threads()
        self.assertEqual(dict_thr['high'], 22)
        self.assertEqual(dict_thr['low'], 11)


if __name__ == '__main__':
    unittest.main()
