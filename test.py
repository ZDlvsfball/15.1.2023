import unittest

from main import Kalkulacka


class KalkulackaTestCase(unittest.TestCase):
    def test_umocni(self):
        x = Kalkulacka()
          # add assertion here
        self.assertEqual(64,x.umocni(4,3))
        self.assertEqual(8,x.umocni(2,3))
        self.assertEqual(-2,x.umocni(0.12,1.3))


    def test_odecti(self):
        x = Kalkulacka()
        self.assertEqual(-23,x.odecti(56,89))
        self.assertEqual(99,x.odecti(67,44444))
        self.assertEqual(-56,x.odecti(5667,3))
        self.assertEqual(34,x.odecti(34,11))

    def test_vydel(self):
        x = Kalkulacka()

        self.assertNotEqual(4,x.vydel(0,3))

if __name__ == '__main__':
    unittest.main()
