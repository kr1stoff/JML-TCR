import unittest
from jml_tcr import get_threads

class MyTestCase(unittest.TestCase):
    def test_get_threads(self):
        # self.assertEqual(True, False)  # add assertion here
        high_threads, low_threads = get_threads()
        self.assertEqual(high_threads, 22)
        self.assertEqual(low_threads, 11)

if __name__ == '__main__':
    unittest.main()
