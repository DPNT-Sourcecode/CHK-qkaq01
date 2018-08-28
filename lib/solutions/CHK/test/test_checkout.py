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

# as you can see in the vid, I forgot to run "continue" on the script. I guess I should have added 10 min or whatever
# to my total time. Sorry about it!

def test_checkout():
    assert 50 == checkout("A")
    assert 50 + 30 == checkout("AB")  # clearer this way
    assert 50 * 2 + 30 == checkout("ABA")
    assert 130 + 45 + 20 == checkout("ABBACA")
    assert 45 + 15 == checkout("BBD")


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
    assert {'A': 1, 'B': 1} == get_amounts("AB")
    assert {'A': 2, 'B': 2, 'C': 1} == get_amounts("ABBCA")
