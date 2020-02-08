from package import main
from webtest import TestApp

app = TestApp(main.app)


def test_functional_v1_status():
    result = app.get("/v1/status")

    assert result.status == "200 OK"
    assert result.json == dict(status="up", version=1)


def test_functional_v2_status():
    result = app.get("/v2/status")

    assert result.status == "200 OK"
    assert result.json == dict(status="up", version=2)


def test_functional_v2_hello():
    result = app.get("/v2/hello/pepe")

    assert result.status == "200 OK"
    assert result.body.decode() == "Hi pepe"
