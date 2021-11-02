import pytest
from hello.hello import hello_world, hello_world_wiki


def test_hello_world():
    assert hello_world() == 'Hello World!'


def test_hello_world_wiki():
    assert len(hello_world_wiki()) > 10


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1
