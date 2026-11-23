from calc import add


def test_add():
    assert add(1, 2) == 3


def test_sub():
    from calc import sub
    assert sub(5, 3) == 2
