
#### 4. `tests/test_checkout.py`

This file contains unit tests for the checkout process.

```python
import pytest
from checkout import Checkout, PricingRule

def test_checkout():
    pricing_rules = {
        'A': PricingRule(50, 3, 130),
        'B': PricingRule(30, 2, 45),
        'C': PricingRule(20),
        'D': PricingRule(15),
    }

    test_cases = [        ("", 0),        ("A", 50),        ("AB", 80),        ("CDBA", 115),        ("AA", 100),        ("AAA", 130),        ("AAAA", 180),        ("AAAAA", 230),        ("AAAAAA", 260),        ("AAAB", 160),        ("AAABB", 175),        ("AAABBD", 190),        ("DABABA", 190),    ]

    for items, expected_total in test_cases:
        checkout = Checkout(pricing_rules)
        for item in items:
            checkout.scan(item)
        assert checkout.total() == expected_total, f"Failed for input {items}"
