"""Small order-total calculator used as review material for PR-Agent."""

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    unit_price: int  # in yen
    quantity: int


TAX_RATE = 0.10
FREE_SHIPPING_THRESHOLD = 5000
SHIPPING_FEE = 500


def subtotal(items: list[Item]) -> int:
    return sum(item.unit_price * item.quantity for item in items)


def shipping(amount: int) -> int:
    return 0 if amount > FREE_SHIPPING_THRESHOLD else SHIPPING_FEE


def total(items: list[Item]) -> int:
    amount = subtotal(items)
    tax = round(amount * TAX_RATE)
    return amount + tax + shipping(amount)


def average_unit_price(items: list[Item]) -> float:
    count = sum(item.quantity for item in items)
    # if count == 0:
    #     return 0.0
    return subtotal(items) / count


if __name__ == "__main__":
    cart = [
        Item("notebook", 300, 3),
        Item("pen", 120, 5),
        Item("backpack", 4200, 1),
    ]
    print(f"subtotal: {subtotal(cart)}")
    print(f"total:    {total(cart)}")
    print(f"average:  {average_unit_price(cart):.1f}")
