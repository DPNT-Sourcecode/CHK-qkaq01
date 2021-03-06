# +------+-------+---------------------------------+
# | Item | Price | Special offers                  |
# +------+-------+---------------------------------+
# | A    | 50    | 3A for 130, 5A for 200          |
# | B    | 30    | 2B for 45                       |
# | C    | 20    |                                 |
# | D    | 15    |                                 |
# | E    | 40    | 2E get one B free               |
# | F    | 10    | 2F get one F free               |
# | G    | 20    |                                 |
# | H    | 10    | 5H for 45, 10H for 80           |
# | I    | 35    |                                 |
# | J    | 60    |                                 |
# | K    | 70    | 2K for 120                      |
# | L    | 90    |                                 |
# | M    | 15    |                                 |
# | N    | 40    | 3N get one M free               |
# | O    | 10    |                                 |
# | P    | 50    | 5P for 200                      |
# | Q    | 30    | 3Q for 80                       |
# | R    | 50    | 3R get one Q free               |
# | S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | U    | 40    | 3U get one U free               |
# | V    | 50    | 2V for 90, 3V for 130           |
# | W    | 20    |                                 |
# | X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
# | Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
# +------+-------+---------------------------------+

# so up until this point I went with the easiest way to add new products, since I didnt know where this was going.
# however now it is obvious that hardcoding prices is not a very maintainable way to do this so let's do some refactoring

from lib.solutions.CHK.checkout_solution import get_amounts, checkout, check_input

def test_get_mix_offer_price():
    assert 45 + 20 == checkout("SSTT")
    assert 45 + 17 + 20 == checkout("STXYZ")


def test_checkout_mixed_products():
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
    assert 50 == checkout("A")
    assert 100 == checkout("AA")
    assert 130 == checkout("AAA")
    assert 180 == checkout("AAAA")
    assert 200 == checkout("AAAAA")
    assert 200 + 50 * 2 == checkout("AAAAAAA")


# lets go step by step and leave the offers like that for now
def test_b_price():
    # Prices without buying any e
    assert 30 == checkout("B")
    assert 45 == checkout("BB")
    assert 75 == checkout("BBB")
    assert 90 + 30 == checkout("BBBBB")
    # Prices buying just one e should be the same
    assert 30 + 40 == checkout("BE")
    assert 45 + 40 == checkout("BBE")
    assert 75 + 40 == checkout("BBBE")
    assert 90 + 30 + 40 == checkout("BBBBBE")
    # Prices buying 2 e should be discounted
    assert 80 == checkout("BEE")
    assert 30 + 80 == checkout("BBEE")
    assert 45 + 80 == checkout("BBBEE")
    assert 45 + 30 + 80 == checkout("BBBBEE")
    # Multiple free Bs
    assert 0 + 4 * 40 == checkout("BBEEEE")


def test_c_price():
    assert 20 == checkout("C")
    assert 40 == checkout("CC")


def test_d_price():
    assert 15 == checkout("D")
    assert 30 == checkout("DD")


def test_e_price():
    assert 40 == checkout("E")
    assert 80 == checkout("EE")


def test_f_price():
    assert 10 == checkout("F")
    assert 20 == checkout("FF")
    assert 20 == checkout("FFF")
    assert 30 == checkout("FFFF")
    assert 40 == checkout("FFFFF")
    assert 40 == checkout("FFFFFF")


def test_super_mix():
    assert 0 < checkout("AABCDEFGHIJKLMNOPQRSTUVWXYZ")


# def test_h_price():
#     # | H    | 10    | 5H for 45, 10H for 80
#     assert 10 == get_h_price(1)
#     assert 40 == get_h_price(4)
#     assert 45 == get_h_price(5)
#     assert 45 + 40 == get_h_price(9)
#     assert 80 == get_h_price(10)
#     assert 80 + 10 == get_h_price(11)
#
#
# def test_k_price():
#     # | K    | 80    | 2K for 150             |
#     assert 80 == get_k_price(1)
#     assert 150 == get_k_price(2)
#     assert 150 + 80 == get_k_price(3)
#
#
# def test_m_price():
#     # | M    | 15    |                        |
#     # | N    | 40    | 3N get one M free
#     assert False
#
#
# def test_n_price():
#     # | N    | 40    | 3N get one M free
#     assert False


def test_get_amounts():
    assert {'A': 1, 'B': 1} == get_amounts("AB")
    assert {'A': 2, 'B': 2, 'C': 1} == get_amounts("ABBCA")


def test_check_input():
    assert check_input("AA")
    assert check_input("AABCD")
    assert check_input("AABCDE")
    assert check_input("AABCDEF")
    assert check_input("AABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert not check_input("AABCDEFGx")


def test_empty_checkout():
    assert check_input("")
