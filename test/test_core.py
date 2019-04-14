import unittest
from .context import core


class TestCore(unittest.TestCase):

    def test_scan_isolated_objects(self):
        cart_items = []
        for x in range(3):
            cart_items.append(core.scan("atv"))

        result = core.checkout(cart_items)

        self.assertEqual(result,
                         {"cart-items": [{"sku": "atv",
                                          "label": "Apple TV",
                                          "price": 109.5,
                                          "promos": [],
                                          "sub-items": []},
                                         {"sku": "atv",
                                          "label": "Apple TV",
                                          "price": 109.5,
                                          "promos": [],
                                          "sub-items": []},
                                         {"sku": "atv",
                                          "label": "Apple TV",
                                          "price": 109.5,
                                          "promos": ["atv-3-for-2"],
                                          "sub-items": [{"label": "3 Apple TVs for 2", "price": -109.5}]}],
                          "total-price": 219.0})

    def test_2_atvs(self):
        cart_items = []
        for x in range(2):
            cart_items.append(core.scan("atv"))

        result = core.checkout(cart_items)
        self.assertEqual(result["total-price"], 219.0)

    def test_3_atvs(self):
        cart_items = []
        for x in range(3):
            cart_items.append(core.scan("atv"))

        result = core.checkout(cart_items)
        self.assertEqual(result["total-price"], 219.0)

    def test_3_ipads(self):
        cart_items = []
        for x in range(3):
            cart_items.append(core.scan("ipd"))

        result = core.checkout(cart_items)
        self.assertEqual(result["total-price"], 1649.97)

    def test_4_ipads(self):
        cart_items = []
        for x in range(4):
            cart_items.append(core.scan("ipd"))

        result = core.checkout(cart_items)
        self.assertEqual(result["total-price"], 1999.96)

    def test_5_ipads(self):
        cart_items = []
        for x in range(5):
            cart_items.append(core.scan("ipd"))

        result = core.checkout(cart_items)
        self.assertEqual(result["total-price"], 2499.95)

    def test_1_mbp(self):
        cart_items = [core.scan("mbp")]

        result = core.checkout(cart_items)
        self.assertEqual(result["cart-items"][0]["sub-items"][0]["sku"], "vga")
        self.assertEqual(result["total-price"], 1399.99)

    def test_preserve_cart_order(self):
        cart_items = []
        for x in range(4):
            cart_items.append(core.scan("atv"))
            cart_items.append(core.scan("ipd"))
            cart_items.append(core.scan("vga"))
        for x in range(4):
            cart_items.append(core.scan("mbp"))

        result = core.checkout(cart_items)
        self.assertEqual(result["cart-items"][1],
                         {"sku": "ipd",
                          "label": "Super iPad",
                          "price": 549.99,
                          "promos": ["ipd-bulk-4"],
                          "sub-items": [{"label": "4+ iPads Bulk Discount", "price": -50.0}]})
        self.assertEqual(result["cart-items"][6],
                         {"sku": "atv",
                          "label": "Apple TV",
                          "price": 109.5,
                          "promos": ["atv-3-for-2"],
                          "sub-items": [{"label": "3 Apple TVs for 2", "price": -109.5}]})
        self.assertEqual(result["cart-items"][2],
                         {"sku": "vga",
                          "label": "VGA adapter",
                          "price": 30.0,
                          "promos": [],
                          "sub-items": []})
        self.assertEqual(result["cart-items"][15],
                         {"sku": "mbp",
                          "label": "MacBook Pro",
                          "price": 1399.99,
                          "promos": ["free-vga-for-macbook-pro"],
                          "sub-items": [{"sku": "vga", "label": "VGA adapter", "price": 0.0}]})


if __name__ == "__main__":
    unittest.main()
