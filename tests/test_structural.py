import unittest

from src.order_calculator import OrderCalculator


class TestOrderCalculatorStatementCoverage(unittest.TestCase):
    """
    Teste pentru statement coverage.
    Scop: sa executam toate instructiunile importante din metoda calculate_final_total
    si din metoda classify_order.
    """

    def setUp(self):
        self.calc = OrderCalculator()

    # Acopera validarea cupoanelor invalide.
    def test_sc_invalid_coupon(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1],
                is_premium=False,
                coupon_percent=40,
                urgent_shipping=False,
            )

    # Acopera validarea valorilor individuale invalide din bucla.
    def test_sc_invalid_price_inside_loop(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10, -5],
                quantities=[1, 1],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # Acopera bulk discount, urgent shipping, bulk extra 3% si cupon.
    def test_sc_all_main_discounts(self):
        result = self.calc.calculate_final_total(
            prices=[20, 30],
            quantities=[10, 10],
            is_premium=True,
            coupon_percent=10,
            urgent_shipping=True,
        )
        self.assertEqual(result, 436.5)

    # Acopera ramura fara premium, fara urgent shipping, fara bulk suplimentar.
    def test_sc_regular_path(self):
        result = self.calc.calculate_final_total(
            prices=[50],
            quantities=[2],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 100.0)

    # Acopera fiecare ramura din classify_order.
    def test_sc_classify_small(self):
        self.assertEqual(self.calc.classify_order(100), "small")

    def test_sc_classify_medium(self):
        self.assertEqual(self.calc.classify_order(300), "medium")

    def test_sc_classify_large(self):
        self.assertEqual(self.calc.classify_order(700), "large")

    def test_sc_classify_invalid(self):
        with self.assertRaises(ValueError):
            self.calc.classify_order(-10)


class TestOrderCalculatorDecisionCoverage(unittest.TestCase):
    """
    Teste pentru decision coverage.
    Scop: fiecare decizie sa fie evaluata o data cu True si o data cu False.
    """

    def setUp(self):
        self.calc = OrderCalculator()

    # D1: len(prices) != len(quantities) or len(prices) == 0 -> True
    def test_dc_invalid_lengths_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1, 2],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # D1 -> False
    def test_dc_invalid_lengths_false(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 10.0)

    # D2: coupon_percent < 0 or coupon_percent > 30 -> True
    def test_dc_invalid_coupon_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1],
                is_premium=False,
                coupon_percent=-1,
                urgent_shipping=False,
            )

    # D2 -> False
    def test_dc_invalid_coupon_false(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[1],
            is_premium=False,
            coupon_percent=10,
            urgent_shipping=False,
        )
        self.assertEqual(result, 9.0)

    # D3: price <= 0 or qty <= 0 -> True
    def test_dc_invalid_line_value_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[0],
                quantities=[1],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # D3 -> False
    def test_dc_invalid_line_value_false(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 10.0)

    # D4: qty >= 10 -> True
    def test_dc_bulk_true(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[10],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 95.0)

    # D4 -> False
    def test_dc_bulk_false(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[9],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 90.0)

    # D5: is_premium and total >= 500 -> True
    def test_dc_premium_discount_true(self):
        result = self.calc.calculate_final_total(
            prices=[500],
            quantities=[1],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 450.0)

    # D5 -> False
    def test_dc_premium_discount_false(self):
        result = self.calc.calculate_final_total(
            prices=[500],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 500.0)

    # D6: urgent_shipping -> True
    def test_dc_urgent_shipping_true(self):
        result = self.calc.calculate_final_total(
            prices=[100],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=True,
        )
        self.assertEqual(result, 125.0)

    # D6 -> False
    def test_dc_urgent_shipping_false(self):
        result = self.calc.calculate_final_total(
            prices=[100],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 100.0)

    # D7: bulk_discount_lines >= 2 -> True
    def test_dc_bulk_lines_true(self):
        result = self.calc.calculate_final_total(
            prices=[10, 20],
            quantities=[10, 10],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 276.45)

    # D7 -> False
    def test_dc_bulk_lines_false(self):
        result = self.calc.calculate_final_total(
            prices=[10, 20],
            quantities=[10, 1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 115.0)

    # D8: final_total < 0 -> True
    def test_dc_classify_invalid_true(self):
        with self.assertRaises(ValueError):
            self.calc.classify_order(-1)

    # D8 -> False
    def test_dc_classify_invalid_false(self):
        self.assertEqual(self.calc.classify_order(50), "small")


class TestOrderCalculatorConditionCoverage(unittest.TestCase):
    """
    Teste pentru condition coverage.
    Urmarim valorile True/False pentru conditiile atomice principale.
    """

    def setUp(self):
        self.calc = OrderCalculator()

    # C1: len(prices) != len(quantities) = True
    def test_cc_len_mismatch_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1, 2],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # C2: len(prices) == 0 = True
    def test_cc_empty_list_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[],
                quantities=[],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # C3: coupon_percent < 0 = True
    def test_cc_coupon_lower_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1],
                is_premium=False,
                coupon_percent=-1,
                urgent_shipping=False,
            )

    # C4: coupon_percent > 30 = True
    def test_cc_coupon_upper_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1],
                is_premium=False,
                coupon_percent=31,
                urgent_shipping=False,
            )

    # C5: price <= 0 = True
    def test_cc_price_invalid_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[0],
                quantities=[1],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # C6: qty <= 0 = True
    def test_cc_qty_invalid_true(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[0],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # C7: is_premium = True, C8: total >= 500 = True
    def test_cc_premium_and_total_true(self):
        result = self.calc.calculate_final_total(
            prices=[500],
            quantities=[1],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 450.0)

    # C7: is_premium = False, C8: total >= 500 = True
    def test_cc_premium_false_total_true(self):
        result = self.calc.calculate_final_total(
            prices=[500],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 500.0)

    # C8: total >= 500 = False
    def test_cc_total_false(self):
        result = self.calc.calculate_final_total(
            prices=[499.99],
            quantities=[1],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 499.99)


if __name__ == "__main__":
    unittest.main(verbosity=2)