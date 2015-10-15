import unittest
from bitcoder.bitcoder import Encoded
from bitcoder.bitcoder import Bool
from bitcoder.bitcoder import Field
from bitcoder.javascript import export


class SimplisticTest(unittest.TestCase):

    def test(self):
        class Example16Bytes(Encoded):
            bits = 16
            gps_enabled = Bool(start=2)
            latitude = Field(start=3, length=4)
            sbas_enabled = Bool(start=10)

        print export(Example16Bytes())

if __name__ == '__main__':
    unittest.main()
