from collections import Counter
import re


def check_input(skus):
    return re.match("^[A-E]*$", skus)


def get_offer_price(amount, offer_amount, offer_price, regular_price):
    (offer, regular) = divmod(amount, offer_amount)
    return offer * offer_price + regular * regular_price


def get_a_price(amount):
    return get_offer_price(amount, 3, 130, 50)


def get_b_price(b_amount, e_amount=0):
    b_free = e_amount // 2
    return get_offer_price(b_amount - b_free, 2, 45, 30)


def get_c_price(amount):
    return amount * 20


def get_d_price(amount):
    return amount * 15


def get_e_price(amount):
    return amount * 40


def get_amounts(skus):
    return Counter(list(skus))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if check_input(skus):
        amounts = get_amounts(skus)
        a = get_a_price(amounts['A'])
        b = get_b_price(amounts['B'])
        c = get_c_price(amounts['C'])
        d = get_d_price(amounts['D'])
        e = get_e_price(amounts['E'])
        return a + b + c + d + e
    else:
        return -1
