from collections import Counter
import re
import json


def check_input(skus):
    return re.match("^[A-Z]*$", skus)


# TODO Still needed?
def get_offer_price(regular_price, amount, offer_amount, offer_price):
    (offer, regular) = divmod(amount, offer_amount)
    return offer * offer_price + regular * regular_price


# Now we can use this to get rid of more hard coding
class same_sku_offer:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


def get_same_sku_offer_price(regular_price, offers, amount):
    total = 0
    to_pay = amount
    for offer in offers:
        if to_pay:
            discounted = to_pay // offer.amount
            if discounted:
                total += discounted * offer.price
                to_pay -= offer.amount  # my goodness not my best day :(
    return total + to_pay * regular_price


def get_free_with_other_offer_price(regular_price, amount, other_amount_buyed, other_amount_offer, same_sku_offers):
    if amount > 0:
        free = other_amount_buyed // other_amount_offer
        return get_same_sku_offer_price(regular_price, same_sku_offers, amount - free)
    else:
        return 0


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

        a_sku = pricesjson['A']
        offers = []
        for o in a_sku['same_sku_offers']:
            offers.append(same_sku_offer(o['amount'], o['price']))  # i never liked been recorderd 0:)
        a = get_same_sku_offer_price(pricesjson['A']['price'], offers, amounts['A'])

        b = get_b_price(pricesjson['B']['price'], amounts['B'], amounts['E'])



        c = amounts['C'] * pricesjson['C']['price']
        d = amounts['D'] * pricesjson['D']['price']
        e = pricesjson['E']['price'] * amounts['E']
        f = get_f_price(amounts['F'])
        return a + b + c + d + e + f
    else:
        return -1
