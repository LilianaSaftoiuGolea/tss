import unittest

from src.order_calculator import OrderCalculator


class TestOrderCalculatorMutationKilling(unittest.TestCase):
    """
    Teste suplimentare pentru a omori mutanti neechivalenti ramasi in viata.
    """

    def setUp(self):
        self.calc = OrderCalculator()

    # 1) Distinge qty >= 10 de qty == 10.
    # Daca mutantul schimba >= in ==, pentru qty = 11 nu ar mai aplica bulk discount.
    def test_mutation_bulk_discount_for_qty_greater_than_10(self):
        result = self.calc.calculate_final_total(
            prices=[10],
            quantities=[11],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 104.5)

    # 2) Distinge total >= 500 de total == 500.
    # Daca mutantul schimba >= in ==, pentru total = 600 nu ar mai aplica discount premium.
    def test_mutation_premium_discount_for_total_greater_than_500(self):
        result = self.calc.calculate_final_total(
            prices=[600],
            quantities=[1],
            is_premium=True,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 540.0)

    # 3) Distinge bulk_discount_lines >= 2 de bulk_discount_lines == 2.
    # Pentru 3 linii bulk, mutantul cu == 2 nu ar mai aplica reducerea suplimentara.
    def test_mutation_bulk_lines_greater_than_2(self):
        result = self.calc.calculate_final_total(
            prices=[10, 20, 30],
            quantities=[10, 10, 10],
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 552.9)

    # 4) Distinge qty <= 0 de qty == 0.
    # Daca mutantul schimba <= in ==, cantitatea negativa nu ar mai fi respinsa.
    def test_mutation_negative_quantity(self):
        with self.assertRaises(ValueError):
            self.calc.calculate_final_total(
                prices=[10],
                quantities=[-1],
                is_premium=False,
                coupon_percent=0,
                urgent_shipping=False,
            )

    # 5) Distinge final_total < 0 de final_total <= 0.
    # Daca mutantul schimba < in <=, valoarea 0 ar deveni invalida in mod gresit.
    def test_mutation_classify_zero(self):
        self.assertEqual(self.calc.classify_order(0), "small")

    # 6) Distinge len(prices) != len(quantities) de len(prices) is not len(quantities).
    # Pentru lungimi egale mari, mutantul cu 'is not' poate da rezultat gresit.
    def test_mutation_large_equal_lengths(self):
        prices = [1.0] * 300
        quantities = [1] * 300

        result = self.calc.calculate_final_total(
            prices=prices,
            quantities=quantities,
            is_premium=False,
            coupon_percent=0,
            urgent_shipping=False,
        )
        self.assertEqual(result, 300.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)