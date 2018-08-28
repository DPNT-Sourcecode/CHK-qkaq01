from collections import Counter


def get_offer_price(amount, offer_amount, offer_price, regular_price):
    (offer, regular) = divmod(amount, offer_amount)
    return offer * offer_price + regular * regular_price


def get_a_price(amount):
    return get_offer_price(amount, 3, 130, 50)


def get_b_price(amount):
    return get_offer_price(amount, 2, 45, 30)


def get_c_price(amount):
    return amount * 20


def get_d_price(amount):
    return amount * 15


def get_amounts(skus):
    return Counter(skus.split())


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    amounts = get_amounts(skus)
    a = get_a_price(amounts['A'])
    b = get_b_price(amounts['B'])
    c = get_c_price(amounts['C'])
    d = get_d_price(amounts['D'])
    return a + b + c + d
