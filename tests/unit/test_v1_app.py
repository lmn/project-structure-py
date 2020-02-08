from unittest import TestCase
from package import v1


class AppTestV1(TestCase):
    def test_status(self):
        assert v1.status() == dict(status="up", version=1)
