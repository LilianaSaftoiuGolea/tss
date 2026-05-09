import unittest

from src.order_calculator import OrderCalculator


class TestOrderCalculatorStructuralAI(unittest.TestCase):
    """Suită structurală autogenerată, orientată pe decizii și căi independente."""

    def setUp(self):
        self.calc = OrderCalculator()

    def assert_total(self, prices, quantities, is_premium, coupon_percent, urgent_shipping, expected):
        total = self.calc.calculate_final_total(
            prices=prices,
            quantities=quantities,
            is_premium=is_premium,
            coupon_percent=coupon_percent,
            urgent_shipping=urgent_shipping,
        )
        self.assertEqual(total, expected)

    def test_independent_paths_for_calculate_final_total(self):
        valid_paths = [
            ("P4_regular_path", [25, 5], [4, 2], False, 0, False, 110.0),
            ("P5_bulk_path", [10, 20], [10, 1], False, 0, False, 115.0),
            ("P6_premium_path", [250, 100], [2, 1], True, 0, False, 540.0),
            ("P7_urgent_shipping_path", [40], [2], False, 0, True, 105.0),
            ("P8_two_bulk_lines_path", [10, 30], [10, 10], False, 0, False, 368.6),
            ("combined_true_branches", [30, 25], [10, 10], True, 10, True, 432.35),
        ]

        for case in valid_paths:
            with self.subTest(path=case[0]):
                self.assert_total(*case[1:])

    def test_error_paths(self):
        error_cases = [
            ("invalid_lengths", [10], [1, 2], False, 0, False),
            ("invalid_coupon_negative", [10], [1], False, -1, False),
            ("invalid_coupon_above_30", [10], [1], False, 31, False),
            ("invalid_value_inside_loop", [10, -3], [1, 2], False, 0, False),
            ("invalid_zero_quantity", [10], [0], False, 0, False),
        ]

        for name, prices, quantities, is_premium, coupon_percent, urgent_shipping in error_cases:
            with self.subTest(path=name):
                with self.assertRaises(ValueError):
                    self.calc.calculate_final_total(
                        prices, quantities, is_premium, coupon_percent, urgent_shipping
                    )

    def test_decision_pairs_true_false(self):
        self.assertEqual(
            self.calc.calculate_final_total([10], [10], False, 0, False), 95.0
        )
        self.assertEqual(
            self.calc.calculate_final_total([10], [9], False, 0, False), 90.0
        )

        self.assertEqual(
            self.calc.calculate_final_total([500], [1], True, 0, False), 450.0
        )
        self.assertEqual(
            self.calc.calculate_final_total([500], [1], False, 0, False), 500.0
        )

        self.assertEqual(
            self.calc.calculate_final_total([100], [1], False, 0, True), 125.0
        )
        self.assertEqual(
            self.calc.calculate_final_total([100], [1], False, 0, False), 100.0
        )

        self.assertEqual(
            self.calc.calculate_final_total([10, 20], [10, 10], False, 0, False), 276.45
        )
        self.assertEqual(
            self.calc.calculate_final_total([10, 20], [10, 1], False, 0, False), 115.0
        )

    def test_classify_all_branches(self):
        branch_cases = [
            (50, "small"),
            (350, "medium"),
            (800, "large"),
        ]

        for total, expected in branch_cases:
            with self.subTest(total=total):
                self.assertEqual(self.calc.classify_order(total), expected)

        with self.assertRaises(ValueError):
            self.calc.classify_order(-0.01)


if __name__ == "__main__":
    unittest.main(verbosity=2)
