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
        # with open('skus.json') as f:
        #     pricesjson = json.load(f)
        pricesjson = get_prices_and_offers() # Im getting the impression Im overthinking / overengineering this
        # Probably the json file parsing was not necessary or expected...
        # Let's keep it simple now

        total_price = 0
        # Lets clean this mess
        for sku_id in pricesjson:
            if amounts[sku_id]:
                sku = pricesjson[sku_id]

                if sku_id == 'S'
                    or sku_id == 'T'
                    or sku_id == 'X'
                    or sku_id == 'Y'
                    or sku_id == 'Z'
                
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

def get_prices_and_offers():
    return {
        "A": {"price": 50,
              "same_sku_offers": [
                  {"amount": 5, "price": 200},
                  {"amount": 3, "price": 130}
              ]
              },
        "B": {"price": 30,
              "free_with_other_offer": {"sku": "E", "amount": 2},
              "same_sku_offers": [
                  {"amount": 2, "price": 45}
              ]
              },
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40},
        "F": {"price": 10,
              "free_with_same_offer": 2
              },
        "G": {"price": 20},
        "H": {"price": 10,
              "same_sku_offers": [
                  {"amount": 10, "price": 80},
                  {"amount": 5, "price": 45}
              ]},
        "I": {"price": 35},
        "J": {"price": 60},
        "K": {"price": 70,
              "same_sku_offers": [
                  {"amount": 2, "price": 150}
              ]
              },
        "L": {"price": 90},
        "M": {"price": 15,
              "free_with_other_offer": {"sku": "N", "amount": 3}
              },
        "N": {"price": 40},
        "O": {"price": 10},
        "P": {"price": 50,
              "same_sku_offers": [
                  {"amount": 5, "price": 200}
              ]
              },
        "Q": {"price": 30,
              "free_with_other_offer": {"sku": "R", "amount": 3},
              "same_sku_offers": [
                  {"amount": 3, "price": 80}
              ]
              },
        "R": {"price": 50},
        "S": {"price": 20},
        "T": {"price": 20},
        "U": {"price": 40,
              "free_with_same_offer": 3
              },
        "V": {"price": 50,
              "same_sku_offers": [
                  {"amount": 3, "price": 130},
                  {"amount": 2, "price": 90}
              ]
              },
        "W": {"price": 20},
        "X": {"price": 17},
        "Y": {"price": 20},
        "Z": {"price": 21}
    }
