from collections import Counter
import re


def check_input(skus):
    return re.match("^[A-Z]*$", skus)


def get_offer_price(amount, offer_amount, offer_price, regular_price):
    (offer, regular) = divmod(amount, offer_amount)
    return offer * offer_price + regular * regular_price


def get_a_price(amount):
    # 3A for 130, 5A for 200
    (offer1, regular) = divmod(amount, 5)
    (offer2, regular) = divmod(regular, 3)
    return offer1 * 200 + offer2 * 130 + regular * 50


def get_b_price(b_amount, e_amount=0):
    if b_amount > 0:
        b_free = e_amount // 2
        return get_offer_price(b_amount - b_free, 2, 45, 30)
    else:
        return 0


def get_c_price(amount):
    return amount * 20


def get_d_price(amount):
    return amount * 15


def get_e_price(amount):
    return amount * 40


def get_f_price(amount):
    free = amount // 3
    return (amount - free) * 10


def get_amounts(skus):
    return Counter(list(skus))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if check_input(skus):
        amounts = get_amounts(skus)
        a = get_a_price(amounts['A'])
        b = get_b_price(amounts['B'],
                        amounts['E'])  # silly mistake... makes me wonder if amount_e shouldnt be optional!
        c = get_c_price(amounts['C'])
        d = get_d_price(amounts['D'])
        e = get_e_price(amounts['E'])
        f = get_f_price(amounts['F'])
        return a + b + c + d + e + f
    else:
        return -1
