import unittest

from src.order_calculator import OrderCalculator


class TestOrderCalculatorEquivalencePartitioning(unittest.TestCase):
    """
    Teste functionale prin partitionare in clase de echivalenta.
    """

    def setUp(self):
        self.calc = OrderCalculator()

    # Clasa valida: comanda obisnuita, fara discounturi.
    def test_valid_regular_order(self):
        result = self.calc.calculate_final_total(
            prices=[10, 20],
            quantities=[2, 3],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 80.0)

    # Clasa valida: exista discount de volum.
    def test_valid_bulk_discount(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[10],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 95.0)

    # Clasa valida: client premium + prag atins.
    def test_valid_premium_discount(self):
        result = self.calc.calculate_final_total(
            prices=[100, 50],
            quantities=[4, 2],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 450.0)

    # Clasa valida: transport urgent.
    def test_valid_urgent_shipping(self):
        result = self.calc.calculate_final_total(
            prices=[50],
            quantities=[2],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=True,
        )
        self.assertEqual(result, 125.0)

    # Clasa valida: doua linii bulk => discount suplimentar de 3%.
    def test_valid_two_bulk_lines(self):
        result = self.calc.calculate_final_total(
            prices=[10, 20],
            quantities=[10, 10],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 276.45)

    # Clasa invalida: liste cu lungimi diferite.
    def test_invalid_mismatched_lengths(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10, 20],
                quantities=[1],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # Clasa invalida: liste vide.
    def test_invalid_empty_lists(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[],
                quantities=[],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # Clasa invalida: pret negativ.
    def test_invalid_negative_price(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[-10],
                quantities=[1],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # Clasa invalida: cantitate zero.
    def test_invalid_zero_quantity(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[0],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # Clasa invalida: cupon negativ.
    def test_invalid_coupon_negative(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1],
                is_premium=False,
                coupon_percent=-1,
                urgent_shipping=False,
            )

    # Clasa invalida: cupon peste limita.
    def test_invalid_coupon_too_large(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[1],
                is_premium=False,
                coupon_percent=31,
                urgent_shipping=False,
            )


class TestOrderCalculatorBoundaryValueAnalysis(unittest.TestCase):
    """
    Teste functionale prin analiza valorilor de frontiera.
    """

    def setUp(self):
        self.calc = OrderCalculator()

    # Frontiera pentru qty: 9 (fara discount bulk).
    def test_boundary_bulk_qty_9(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[9],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 90.0)

    # Frontiera pentru qty: 10 (cu discount bulk).
    def test_boundary_bulk_qty_10(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[10],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 95.0)

    # Frontiera inferioara pentru cupon.
    def test_boundary_coupon_0(self):
        result = self.calc.calculate_final_total(
            prices=[100],
            quantities=[1],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 100.0)

    # Frontiera superioara valida pentru cupon.
    def test_boundary_coupon_30(self):
        result = self.calc.calculate_final_total(
            prices=[100],
            quantities=[1],
            is_premium=False,
            coupon_percent=30,
            urgent_shipping=False,
        )
        self.assertEqual(result, 70.0)

    # Sub frontiera inferioara pentru cupon.
    def test_boundary_coupon_minus_1(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[100],
                quantities=[1],
                is_premium=False,
                coupon_percent=-1,
                urgent_shipping=False,
            )

    # Peste frontiera superioara pentru cupon.
    def test_boundary_coupon_31(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[100],
                quantities=[1],
                is_premium=False,
                coupon_percent=31,
                urgent_shipping=False,
            )

    # Frontiera premium total sub pragul 500.
    def test_boundary_premium_total_just_below_500(self):
        result = self.calc.calculate_final_total(
            prices=[499.99],
            quantities=[1],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 499.99)

    # Frontiera premium total exact 500.
    def test_boundary_premium_total_exact_500(self):
        result = self.calc.calculate_final_total(
            prices=[500],
            quantities=[1],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 450.0)

    # Frontiere pentru clasificare: 199.99 / 200 / 500 / 500.01
    def test_boundary_classify_small(self):
        self.assertEqual(self.calc.classify_order(199.99), "small")

    def test_boundary_classify_medium_lower(self):
        self.assertEqual(self.calc.classify_order(200), "medium")

    def test_boundary_classify_medium_upper(self):
        self.assertEqual(self.calc.classify_order(500), "medium")

    def test_boundary_classify_large(self):
        self.assertEqual(self.calc.classify_order(500.01), "large")

    # Frontiera invalida pentru clasificare.
    def test_boundary_classify_negative(self):
        with self.assertRaises(ValueError):
            self.calc.classify_order(-1)


if __name__ == "__main__":
    unittest.main(verbosity=2)