import unittest
from package import v2


class AppTestV2(unittest.TestCase):
    def test_status(self):
        assert v2.status() == dict(status="up", version=2)

    def test_hello(self):
        assert v2.hello("pepe") == "Hi pepe"
