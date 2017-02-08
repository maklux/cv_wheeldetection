import unittest
from circle import Circle

class TestCircle(unittest.TestCase):
    def test_init(self):
        self.assertEquals('test', Circle('test').filename)

if __name__ == '__main__':
    unittest.main()
