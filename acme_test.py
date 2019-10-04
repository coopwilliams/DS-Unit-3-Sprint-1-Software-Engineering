#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, inventory_report, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """ Test default product weight being 20. """
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealable_explosive(self):
        """ Test for products that are highly stealable and explosive """
        prod = Product('Test Bomb', price=21, flammability=1000)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")

class AcmeReportTests(unittest.TestCase):
    """ Test that Acme Report is working. """

    def test_default_num_products(self):
        """ Test that the default num_products is correct. """
        items = generate_products()
        self.assertEqual(len(items), 30)

    def test_legal_names(self):
        """ Test that generated product names are legal. """
        items = generate_products()
        adjectives = list(i.name.split(' ')[0] for i in items)
        nouns = list(i.name.split(' ', 1)[1] for i in items)
        for i in adjectives:
            self.assertIn(i, ADJECTIVES)
        for i in nouns:
            self.assertIn(i, NOUNS)

    def test_printout(self):
        """ Test that inventory_report prints correctly """
        import sys
        from io import StringIO
        from unittest.mock import patch

        with patch('sys.stdout', new=StringIO()) as output:
            items = generate_products()
            inventory_report(items)
            self.assertIn("ACME CORPORATION OFFICIAL INVENTORY REPORT",
                            output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
