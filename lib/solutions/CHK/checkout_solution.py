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
class SameSkuOffer:
    def __init__(self, amount, price):
        self.amount = amount
        self.price = price


class FreeWithOtherSkuOffer:
    def __init__(self, sku, amount):
        self.sku = sku
        self.amount = amount


def get_same_sku_offer_price(regular_price, offers, amount):
    total = 0
    to_pay = amount
    for offer in offers:
        if to_pay:
            discounted = to_pay // offer.amount
            if discounted:
                total += discounted * offer.price
                to_pay -= offer.amount * discounted  # my goodness not my best day :(
    return total + to_pay * regular_price


def get_free_with_other_offer_price(regular_price, amount, other_amount_buyed, other_amount_offer, same_sku_offers):
    if amount > 0:
        # for o in free_other_sku_offers: # lets not complicate this too much. lets assume one one "free with" offer can be have
        free = other_amount_buyed // other_amount_offer
        return get_same_sku_offer_price(regular_price, same_sku_offers, amount - free)
    else:
        return 0


# Finally we can use this to further parametrize the system
def get_free_with_same_offer_price(regular_price, amount, offer_buy):
    free = 0
    if amount >= offer_buy + 1:
        free = amount // (offer_buy + 1)
    return (amount - free) * regular_price


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
        offers = get_same_sku_offers(a_sku)
        a = get_same_sku_offer_price(a_sku['price'], offers, amounts['A'])

        b_sku = pricesjson['B']
        offers = get_same_sku_offers(b_sku)
        free_with_offer = FreeWithOtherSkuOffer(b_sku['free_with_other_offer']['sku'],
                                                b_sku['free_with_other_offer']['amount'])
        b = get_free_with_other_offer_price(b_sku['price'], amounts['B'], amounts[free_with_offer.sku],
                                            free_with_offer.amount, offers)

        c = amounts['C'] * pricesjson['C']['price']
        d = amounts['D'] * pricesjson['D']['price']
        e = amounts['E'] * pricesjson['E']['price']

        f_sku = pricesjson['F']
        free_with_same_offer = f_sku['free_with_same_offer']
        f = get_free_with_same_offer_price(f_sku['price'], amounts['F'], free_with_same_offer)

        return a + b + c + d + e + f
    else:
        return -1


def get_same_sku_offers(sku):
    offers = []
    for o in sku['same_sku_offers']:
        offers.append(SameSkuOffer(o['amount'], o['price']))  # i never liked been recorderd 0:)
    return offers
