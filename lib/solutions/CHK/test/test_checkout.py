# +------+-------+------------------------+
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      | # Just making sure nothing else has changed
# +------+-------+------------------------+

from lib.solutions.CHK.checkout_solution import get_a_price, get_b_price, get_c_price, get_d_price, get_amounts, \
    checkout, check_input, get_e_price


def test_checkout():
    assert 50 == checkout("A")
    assert 50 + 30 == checkout("AB")  # clearer this way
    assert 50 * 2 + 30 == checkout("ABA")
    assert 130 + 45 + 20 == checkout("ABBACA")
    assert 45 + 15 == checkout("BBD")

    assert 80 == checkout("EEB")
    assert 80 == checkout("EE")

    assert 10 == checkout("F")
    assert 20 == checkout("FF")
    assert 20 == checkout("FFF")


def test_a_price():
    assert 50 == get_a_price(1)
    assert 100 == get_a_price(2)
    assert 130 == get_a_price(3)
    assert 180 == get_a_price(4)
    assert 200 == get_a_price(5)
    assert 200 + 50 * 2 == get_a_price(7)


def test_b_price():
    # Prices without buying any e
    assert 30 == get_b_price(b_amount=1, e_amount=0)
    assert 45 == get_b_price(b_amount=2, e_amount=0)
    assert 75 == get_b_price(b_amount=3, e_amount=0)
    assert 90 + 30 == get_b_price(b_amount=5, e_amount=0)
    # Prices buying just one e should be the same
    assert 30 == get_b_price(b_amount=1, e_amount=1)
    assert 45 == get_b_price(b_amount=2, e_amount=1)
    assert 75 == get_b_price(b_amount=3, e_amount=1)
    assert 90 + 30 == get_b_price(b_amount=5, e_amount=1)
    # Prices buying 2 e should be discounted
    assert 0 == get_b_price(b_amount=1, e_amount=2)
    assert 30 == get_b_price(b_amount=2, e_amount=2)
    assert 45 == get_b_price(b_amount=3, e_amount=2)
    assert 45 * 2 == get_b_price(b_amount=5, e_amount=2)
    # Multiple free Bs
    assert 0 == get_b_price(b_amount=2, e_amount=4)


def test_c_price():
    assert 20 == get_c_price(1)
    assert 40 == get_c_price(2)


def test_d_price():
    assert 15 == get_d_price(1)
    assert 30 == get_d_price(2)


def test_e_price():
    assert 40 == get_e_price(1)
    assert 80 == get_e_price(2)

def test_f_price():
    assert 10 == get_f_price(1)
    assert 20 == get_f_price(2)
    assert 20 == get_f_price(3)

def test_get_amounts():
    assert {'A': 1, 'B': 1} == get_amounts("AB")
    assert {'A': 2, 'B': 2, 'C': 1} == get_amounts("ABBCA")


def test_check_input():
    assert check_input("AA")
    assert check_input("AABCD")
    assert check_input("AABCDE")
    assert not check_input("AABCDEF")
    assert not check_input("AABCDEFx")


def test_empty_checkout():
    assert check_input("")
