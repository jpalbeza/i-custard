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


def tag_all_macbook_pro(cart_items):
    for item in cart_items:
        if item["sku"] == "mbp":
            item["promos"].append("free-vga-for-macbook-pro")


def free_vga():
    vga = copy.deepcopy(catalogue.products["vga"])
    vga["price"] = 0.0

    return vga


promos = {"atv-3-for-2": {"tag-applicable": tag_every_3rd_atv,
                          "promo-item": {"label": "3 Apple TVs for 2",
                                         "price": (-1 * catalogue.products["atv"]["price"])}},
          "ipd-bulk-4": {"tag-applicable": tag_bulk_ipd,
                         "promo-item": {"label": "4+ iPads Bulk Discount",
                                        "price": (-1 * (catalogue.products["ipd"]["price"] - 499.99))}},
          "free-vga-for-macbook-pro": {"tag-applicable": tag_all_macbook_pro,
                                       "promo-item": free_vga()}}


def tag_with_promos(cart_items):
    for promo_value in promos.values():
        promo_value["tag-applicable"](cart_items)


def apply_promos(cart_items):
    for item in cart_items:
        for promo in item["promos"]:
            promo_item = copy.deepcopy(promos[promo]["promo-item"])
            item["sub-items"].append(promo_item)
