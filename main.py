from checkout import Checkout, PricingRule

def main():
    pricing_rules = {
        'A': PricingRule(50, 3, 130),
        'B': PricingRule(30, 2, 45),
        'C': PricingRule(20),
        'D': PricingRule(15),
    }

    checkout = Checkout(pricing_rules)

    items = input("Enter the items: ")
    for item in items:
        checkout.scan(item)

    print(f"Total price for items '{items}': {checkout.total()}")

if __name__ == "__main__":
    main()
