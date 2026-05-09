import unittest

from src.order_calculator import OrderCalculator


class TestOrderCalculatorFunctionalAI(unittest.TestCase):
    """Suită funcțională autogenerată, mai complexă și orientată pe scenarii."""

    def setUp(self):
        self.default_calc = OrderCalculator()
        self.custom_calc = OrderCalculator(urgent_shipping_fee=40.0)

    def test_valid_scenarios_table_driven(self):
        cases = [
            {
                "name": "regular_order_without_discounts",
                "prices": [19.99, 5.5],
                "quantities": [2, 3],
                "is_premium": False,
                "coupon_percent": 0,
                "urgent_shipping": False,
                "expected": 56.48,
            },
            {
                "name": "bulk_and_coupon_without_premium",
                "prices": [15, 40],
                "quantities": [10, 2],
                "is_premium": False,
                "coupon_percent": 20,
                "urgent_shipping": False,
                "expected": 178.0,
            },
            {
                "name": "premium_exactly_over_business_threshold",
                "prices": [500],
                "quantities": [1],
                "is_premium": True,
                "coupon_percent": 15,
                "urgent_shipping": False,
                "expected": 382.5,
            },
            {
                "name": "premium_urgent_two_bulk_lines_and_coupon",
                "prices": [30, 25, 10],
                "quantities": [10, 10, 5],
                "is_premium": True,
                "coupon_percent": 5,
                "urgent_shipping": True,
                "expected": 497.84,
            },
        ]

        for case in cases:
            with self.subTest(case=case["name"]):
                total = self.default_calc.calculate_final_total(
                    prices=case["prices"],
                    quantities=case["quantities"],
                    is_premium=case["is_premium"],
                    coupon_percent=case["coupon_percent"],
                    urgent_shipping=case["urgent_shipping"],
                )
                self.assertEqual(total, case["expected"])

    def test_custom_shipping_fee_changes_result(self):
        total = self.custom_calc.calculate_final_total(
            prices=[100, 20],
            quantities=[2, 5],
            is_premium=False,
            coupon_percent=10,
            urgent_shipping=True,
        )
        self.assertEqual(total, 306.0)

    def test_boundaries_for_coupon_and_quantity(self):
        quantity_cases = [
            ("quantity_9_no_bulk", [15], [9], False, 0, False, 135.0),
            ("quantity_10_with_bulk", [15], [10], False, 0, False, 142.5),
        ]

        coupon_cases = [
            ("coupon_0", [200], [1], False, 0, False, 200.0),
            ("coupon_30", [200], [1], False, 30, False, 140.0),
        ]

        for name, prices, quantities, is_premium, coupon_percent, urgent_shipping, expected in quantity_cases + coupon_cases:
            with self.subTest(case=name):
                total = self.default_calc.calculate_final_total(
                    prices=prices,
                    quantities=quantities,
                    is_premium=is_premium,
                    coupon_percent=coupon_percent,
                    urgent_shipping=urgent_shipping,
                )
                self.assertEqual(total, expected)

    def test_invalid_inputs_table_driven(self):
        invalid_cases = [
            ("empty_lists", [], [], False, 0, False),
            ("mismatched_lengths", [10, 20], [1], False, 0, False),
            ("zero_price", [0], [1], False, 0, False),
            ("negative_price", [-10], [1], False, 0, False),
            ("zero_quantity", [10], [0], False, 0, False),
            ("negative_quantity", [10], [-3], False, 0, False),
            ("coupon_minus_one", [10], [1], False, -1, False),
            ("coupon_thirty_one", [10], [1], False, 31, False),
        ]

        for name, prices, quantities, is_premium, coupon_percent, urgent_shipping in invalid_cases:
            with self.subTest(case=name):
                with self.assertRaises(ValueError):
                    self.default_calc.calculate_final_total(
                        prices=prices,
                        quantities=quantities,
                        is_premium=is_premium,
                        coupon_percent=coupon_percent,
                        urgent_shipping=urgent_shipping,
                    )

    def test_classification_boundaries_table_driven(self):
        classification_cases = [
            (199.99, "small"),
            (200, "medium"),
            (350.75, "medium"),
            (500, "medium"),
            (500.01, "large"),
        ]

        for total, expected_label in classification_cases:
            with self.subTest(total=total):
                self.assertEqual(self.default_calc.classify_order(total), expected_label)

    def test_negative_total_for_classification_is_rejected(self):
        with self.assertRaises(ValueError):
            self.default_calc.classify_order(-0.5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
