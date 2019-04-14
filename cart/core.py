import copy
from cart import catalogue, promos


initial_scan_data = {"promos": [], "sub-items": []}


def scan(sku):
    scanned_item = copy.deepcopy(catalogue.products[sku])
    scanned_item.update(copy.deepcopy(initial_scan_data))

    return scanned_item


def get_total_price(cart_items):
    total_price = 0
    for item in cart_items:
        sub_items_total = sum(sub_item["price"] for sub_item in item["sub-items"])
        total_price += item["price"] + sub_items_total

    return total_price
