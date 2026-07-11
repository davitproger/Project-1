# GitHub username: davitproger
# Date: July 10, 2026
# Description: Contains unit tests for the MenuItem and LemonadeStand classes.

import unittest

from LemonadeStand import (
    MenuItem,
    LemonadeStand,
    DuplicateMenuItemError,
    MissingMenuItemError
)


class LemonadeStandTester(unittest.TestCase):
    """Tests the MenuItem and LemonadeStand classes."""

    def test_menu_item_name(self):
        item = MenuItem("lemonade", 0.50, 1.50)

        self.assertEqual(item.get_name(), "lemonade")

    def test_menu_item_prices(self):
        item = MenuItem("iced tea", 0.40, 1.25)

        self.assertEqual(item.get_wholesale_cost(), 0.40)
        self.assertEqual(item.get_selling_price(), 1.25)

    def test_stand_name(self):
        stand = LemonadeStand("Lemons R Us")

        self.assertEqual(stand.get_name(), "Lemons R Us")

    def test_enter_sales(self):
        stand = LemonadeStand("Lemons R Us")
        item = MenuItem("lemonade", 0.50, 1.50)

        stand.add_menu_item(item)
        stand.enter_sales("lemonade", 10)
        stand.enter_sales("lemonade", 5)

        self.assertEqual(stand.number_of_item_sold("lemonade"), 15)

    def test_profit_margin_for_item(self):
        stand = LemonadeStand("Lemons R Us")
        item = MenuItem("lemonade", 0.50, 1.50)

        stand.add_menu_item(item)

        self.assertAlmostEqual(
            stand.profit_margin_for_item("lemonade"),
            1.00
        )

    def test_total_profit_for_stand(self):
        stand = LemonadeStand("Lemons R Us")

        lemonade = MenuItem("lemonade", 0.50, 1.50)
        iced_tea = MenuItem("iced tea", 0.40, 1.40)

        stand.add_menu_item(lemonade)
        stand.add_menu_item(iced_tea)

        stand.enter_sales("lemonade", 10)
        stand.enter_sales("iced tea", 5)

        self.assertAlmostEqual(
            stand.total_profit_for_stand(),
            15.00
        )

    def test_duplicate_menu_item_error(self):
        stand = LemonadeStand("Lemons R Us")

        first_item = MenuItem("lemonade", 0.50, 1.50)
        second_item = MenuItem("lemonade", 0.60, 1.75)

        stand.add_menu_item(first_item)

        with self.assertRaises(DuplicateMenuItemError):
            stand.add_menu_item(second_item)

    def test_missing_menu_item_error(self):
        stand = LemonadeStand("Lemons R Us")

        with self.assertRaises(MissingMenuItemError):
            stand.enter_sales("coffee", 5)


if __name__ == "__main__":
    unittest.main()