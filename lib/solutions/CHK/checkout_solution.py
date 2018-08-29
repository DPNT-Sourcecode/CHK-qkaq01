from collections import Counter
import re
import json


def check_input(skus):
    return re.match("^[A-Z]*$", skus)


def get_offer_price(regular_price, amount, offer_amount, offer_price):
    (offer, regular) = divmod(amount, offer_amount)
    return offer * offer_price + regular * regular_price


class same_sku_offer:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


def get_same_sku_offer_price(regular_price, offers, amount):
    total = 0
    to_pay = amount
    for offer in offers:
        (discounted, to_pay) = divmod(amount, offer.amount)
        if discounted:
            total += discounted * offer.price
            # to_pay -= offer.amount
    return total + to_pay * regular_price


def get_a_price(regular_price, amount):
    # 3A for 130, 5A for 200
    # (offer1, regular) = divmod(amount, 5)
    # (offer2, regular) = divmod(regular, 3)
    # return offer1 * 200 + offer2 * 130 + regular * regular_price
    offers = [
        same_sku_offer(3, 130),
        same_sku_offer(5, 200)
    ]
    return get_same_sku_offer_price(regular_price, offers, amount)

def get_b_price(regular_price, b_amount, e_amount=0):
    if b_amount > 0:
        b_free = e_amount // 2
        return get_offer_price(regular_price, b_amount - b_free, 2, 45, )
    else:
        return 0


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
        with open('skus.json') as f:
            pricesjson = json.load(f)

        a = get_a_price(pricesjson['A']['price'], amounts['A'])
        b = get_b_price(pricesjson['B']['price'], amounts['B'], amounts['E'])
        c = amounts['C'] * pricesjson['C']['price']
        d = amounts['D'] * pricesjson['D']['price']
        e = pricesjson['E']['price'] * amounts['E']
        f = get_f_price(amounts['F'])
        return a + b + c + d + e + f
    else:
        return -1
