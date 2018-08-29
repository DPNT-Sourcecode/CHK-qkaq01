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

        total_price = 0
        # Lets clean this mess
        for sku_id in pricesjson:
            if amounts[sku_id]:
                sku = pricesjson[sku_id] # getting too tired/anxious i guess
                same_sku_offers = get_same_sku_offers(sku)
                free_with_other_offer = get_free_with_other_sku_offers(sku)
                free_with_same_offer = sku['free_with_same_offer'] if 'free_with_same_offer' in sku else None

                if free_with_other_offer:
                    total_price += get_free_with_other_offer_price(sku['price'], amounts[sku_id], amounts[free_with_other_offer.sku],
                                                             free_with_other_offer.amount, same_sku_offers)
                elif same_sku_offers:
                    total_price += get_same_sku_offer_price(sku['price'], same_sku_offers, amounts[sku_id])
                elif free_with_same_offer:
                    total_price += get_free_with_same_offer_price(sku['price'], amounts[sku_id], free_with_same_offer)
                else: # of course, the simplest case! :)
                    total_price += amounts[sku_id] * pricesjson[sku_id]['price']

        return total_price
    else:
        return -1


def get_same_sku_offers(sku):
    offers = []
    if 'same_sku_offers' in sku:
        for o in sku['same_sku_offers']:
            offers.append(SameSkuOffer(o['amount'], o['price']))  # i never liked been recorderd 0:)
    return offers


def get_free_with_other_sku_offers(sku):
    if 'free_with_other_offer' in sku:
        return FreeWithOtherSkuOffer(sku['free_with_other_offer']['sku'],
                                       sku['free_with_other_offer']['amount'])
    else:
        return None
