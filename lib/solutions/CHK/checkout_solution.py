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


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    raise NotImplementedError()
