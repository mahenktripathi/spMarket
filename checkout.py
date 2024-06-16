class PricingRule:
    def __init__(self, price, discount_count=None, discount_price=None):
        self.price = price
        self.discount_count = discount_count
        self.discount_price = discount_price

class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = {}

    def scan(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def total(self):
        total = 0
        for item, count in self.items.items():
            if item in self.pricing_rules:
                rule = self.pricing_rules[item]
                if rule.discount_count and rule.discount_price:
                    total += (count // rule.discount_count) * rule.discount_price
                    total += (count % rule.discount_count) * rule.price
                else:
                    total += count * rule.price
            else:
                raise ValueError(f"No pricing rule defined for item '{item}'")
        return total
