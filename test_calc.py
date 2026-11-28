from calc import add


def test_add():
    assert add(1, 2) == 3


def test_multiply():
    from calc import multiply
    assert multiply(3, 4) == 12
