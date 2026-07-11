# GitHub username: davitproger
# Date: July 10, 2026
# Description: Defines MenuItem and LemonadeStand classes for tracking
# menu items, sales, and profit.


class DuplicateMenuItemError(Exception):
    """Raised when a menu item with the same name already exists."""
    pass


class MissingMenuItemError(Exception):
    """Raised when a requested menu item does not exist."""
    pass


class MenuItem:
    """Represents an item sold at a lemonade stand."""

    def __init__(self, name, wholesale_cost, selling_price):
        self.__name = name
        self.__wholesale_cost = wholesale_cost
        self.__selling_price = selling_price

    def get_name(self):
        """Returns the name of the menu item."""
        return self.__name

    def get_wholesale_cost(self):
        """Returns the wholesale cost of the menu item."""
        return self.__wholesale_cost

    def get_selling_price(self):
        """Returns the selling price of the menu item."""
        return self.__selling_price


class LemonadeStand:
    """Represents a lemonade stand with menu items and sales records."""

    def __init__(self, name):
        self.__name = name
        self.__menu = {}
        self.__sales_record = {}

    def get_name(self):
        """Returns the name of the lemonade stand."""
        return self.__name

    def add_menu_item(self, menu_item):
        """Adds a MenuItem object to the stand's menu."""
        item_name = menu_item.get_name()

        if item_name in self.__menu:
            raise DuplicateMenuItemError

        self.__menu[item_name] = menu_item
        self.__sales_record[item_name] = 0

    def enter_sales(self, item_name, number_sold):
        """Adds the number sold to the sales record for an item."""
        if item_name not in self.__menu:
            raise MissingMenuItemError

        self.__sales_record[item_name] += number_sold

    def number_of_item_sold(self, item_name):
        """Returns the total number sold for a menu item."""
        if item_name not in self.__menu:
            raise MissingMenuItemError

        return self.__sales_record[item_name]

    def profit_margin_for_item(self, item_name):
        """Returns the profit made from selling one unit of an item."""
        if item_name not in self.__menu:
            raise MissingMenuItemError

        menu_item = self.__menu[item_name]

        selling_price = menu_item.get_selling_price()
        wholesale_cost = menu_item.get_wholesale_cost()

        return selling_price - wholesale_cost

    def total_profit_for_stand(self):
        """Returns the total profit for all items sold."""
        total_profit = 0

        for item_name in self.__menu:
            number_sold = self.number_of_item_sold(item_name)
            profit_margin = self.profit_margin_for_item(item_name)

            total_profit += number_sold * profit_margin

        return total_profit


def main():
    """Demonstrates the LemonadeStand and MenuItem classes."""
    stand = LemonadeStand("Lemons R Us")

    lemonade = MenuItem("lemonade", 0.50, 1.50)
    iced_tea = MenuItem("iced tea", 0.40, 1.25)

    stand.add_menu_item(lemonade)
    stand.add_menu_item(iced_tea)

    stand.enter_sales("lemonade", 18)
    stand.enter_sales("iced tea", 10)

    print("Stand name:", stand.get_name())
    print("Lemonades sold:", stand.number_of_item_sold("lemonade"))
    print("Total profit:", stand.total_profit_for_stand())

    try:
        stand.enter_sales("coffee", 5)

    except MissingMenuItemError:
        print("Error: coffee is not on the lemonade stand's menu.")


if __name__ == "__main__":
    main()