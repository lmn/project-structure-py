from package import v1
from webtest import TestApp


def test_functional_status():
    app = TestApp(v1.app)

    assert app.get("/status").status == "200 OK"
