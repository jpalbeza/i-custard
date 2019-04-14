import copy
from cart import catalogue


def tag_every_3rd_atv(cart_items):
    apple_tv_count = 0

    for item in cart_items:
        if item["sku"] == "atv":
            apple_tv_count += 1
            if apple_tv_count == 3:
                item["promos"].append("atv-3-for-2")
                apple_tv_count = 0


def free_atv(item):
    item["sub-items"].append(copy.deepcopy({"label": "3 Apple TVs for 2",
                                            "price": (-1 * catalogue.products["atv"]["price"])}))


def tag_bulk_ipd(cart_items):
    ipad_count = 0
    for item in cart_items:
        if item["sku"] == "ipd":
            ipad_count += 1
            if ipad_count >= 4:
                break;

    if ipad_count >= 4:
        for item in cart_items:
            if item["sku"] == "ipd":
                item["promos"].append("ipd-bulk-4")


def discounted_ipd(item):
    target_price = 499.99
    item["sub-items"].append(copy.deepcopy({"label": "4 iPads Bulk Discount",
                                            "price": (-1 * (catalogue.products["ipd"]["price"] - target_price))}))


promos = {"atv-3-for-2": {"tag-applicable": tag_every_3rd_atv,
                          "apply-promo": free_atv},
          "ipd-bulk-4": {"tag-applicable": tag_bulk_ipd,
                         "apply-promo": discounted_ipd}}


def tag_with_promos(cart_items):
    for promo_value in promos.values():
        promo_value["tag-applicable"](cart_items)


def apply_promos(cart_items):
    for item in cart_items:
        for promo in item["promos"]:
            promos[promo]["apply-promo"](item)
