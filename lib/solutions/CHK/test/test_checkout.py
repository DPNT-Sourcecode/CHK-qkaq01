# +------+-------+----------------+
# | Item | Price | Special offers |
# +------+-------+----------------+
# | A    | 50    | 3A for 130     |
# | B    | 30    | 2B for 45      |
# | C    | 20    |                |
# | D    | 15    |                |
# +------+-------+----------------+

from lib.solutions.CHK.checkout_solution import get_a_price, get_b_price, get_c_price, get_d_price, get_amounts, \
    checkout


def test_checkout():
    assert 50 == checkout("A")


def test_a_price():
    assert 50 == get_a_price(1)
    assert 100 == get_a_price(2)
    assert 130 == get_a_price(3)
    assert 180 == get_a_price(4)
    assert 310 == get_a_price(7)


def test_b_price():
    assert 30 == get_b_price(1)
    assert 45 == get_b_price(2)
    assert 75 == get_b_price(3)
    assert 90 + 30 == get_b_price(5)


def test_c_price():
    assert 20 == get_c_price(1)
    assert 40 == get_c_price(2)


def test_d_price():
    assert 15 == get_d_price(1)
    assert 30 == get_d_price(2)


def test_get_amounts():
    assert {'A': 1, 'B': 1} == get_amounts("A B")
    assert {'A': 2, 'B': 2, 'C': 1} == get_amounts("A B B C A")
