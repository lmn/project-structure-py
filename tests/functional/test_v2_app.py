from package import v2
from webtest import TestApp

app = TestApp(v2.app)


def test_functional_status():
    assert app.get("/status").status == "200 OK"
