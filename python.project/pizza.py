def make_pizza(size, *toppings):
    """Make a pizza with the given size and toppings."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"  - {topping}")
