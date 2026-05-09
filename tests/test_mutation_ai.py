import unittest

from src.order_calculator import OrderCalculator


class TestOrderCalculatorMutationAI(unittest.TestCase):
    """Suită autogenerată orientată pe praguri sensibile pentru mutation testing."""

    def setUp(self):
        self.calc = OrderCalculator()

    def test_threshold_sensitive_cases(self):
        threshold_cases = [
            ("qty_greater_than_10", [10], [11], False, 0, False, 104.5),
            ("premium_total_strictly_greater_than_500", [510], [1], True, 0, False, 459.0),
            ("three_bulk_lines", [10, 20, 30], [10, 10, 10], False, 0, False, 552.9),
            ("coupon_upper_valid_boundary", [100], [1], False, 30, False, 70.0),
        ]

        for case in threshold_cases:
            with self.subTest(case=case[0]):
                total = self.calc.calculate_final_total(
                    prices=case[1],
                    quantities=case[2],
                    is_premium=case[3],
                    coupon_percent=case[4],
                    urgent_shipping=case[5],
                )
                self.assertEqual(total, case[6])

    def test_invalid_values_relevant_for_mutants(self):
        invalid_cases = [
            ("negative_quantity", [5], [-1], False, 0, False),
            ("negative_price", [-5], [1], False, 0, False),
            ("coupon_31", [100], [1], False, 31, False),
        ]

        for name, prices, quantities, is_premium, coupon_percent, urgent_shipping in invalid_cases:
            with self.subTest(case=name):
                with self.assertRaises(ValueError):
                    self.calc.calculate_final_total(
                        prices, quantities, is_premium, coupon_percent, urgent_shipping
                    )

    def test_classification_sensitive_cases(self):
        self.assertEqual(self.calc.classify_order(0), "small")
        self.assertEqual(self.calc.classify_order(500), "medium")
        self.assertEqual(self.calc.classify_order(500.01), "large")

    def test_large_equal_lengths_case(self):
        prices = [1.0] * 300
        quantities = [1] * 300
        total = self.calc.calculate_final_total(prices, quantities, False, 0, False)
        self.assertEqual(total, 300.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
