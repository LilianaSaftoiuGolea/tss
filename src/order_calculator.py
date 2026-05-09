from typing import List


class OrderCalculator:
    """
    Clasa gestioneaza calculul totalului final al unei comenzi
    si clasificarea acesteia in functie de valoare.
    """

    def __init__(self, urgent_shipping_fee: float = 25.0) -> None:
        # Taxa fixa pentru transport urgent.
        self.urgent_shipping_fee = urgent_shipping_fee

    def calculate_final_total(
        self,
        prices: List[float],
        quantities: List[int],
        is_premium: bool,
        coupon_percent: int,
        urgent_shipping: bool,
    ) -> float:
        """
        Calculeaza totalul final al unei comenzi.

        Parametri:
        - prices: lista preturilor unitare
        - quantities: lista cantitatilor corespunzatoare
        - is_premium: True daca utilizatorul este premium
        - coupon_percent: procent cupon intre 0 si 30
        - urgent_shipping: True daca se doreste transport urgent

        Reguli:
        1. prices si quantities trebuie sa aiba aceeasi lungime si sa nu fie vide;
        2. fiecare pret si cantitate trebuie sa fie strict pozitive;
        3. coupon_percent trebuie sa fie intre 0 si 30;
        4. pentru o linie cu qty >= 10 se aplica discount de volum de 5%;
        5. daca utilizatorul este premium si totalul intermediar >= 500,
           se aplica discount suplimentar de 10%;
        6. daca urgent_shipping este True, se adauga taxa fixa de transport;
        7. daca exista cel putin 2 linii cu discount de volum, se mai aplica 3%;
        8. la final se aplica si cuponul.
        """

        # Validare lungimi liste.
        if len(prices) != len(quantities) or len(prices) == 0:
            raise ValueError("prices si quantities trebuie sa aiba aceeasi lungime nenula.")

        # Validare procent cupon.
        if coupon_percent < 0 or coupon_percent > 30:
            raise ValueError("coupon_percent trebuie sa fie intre 0 si 30.")

        total = 0.0
        bulk_discount_lines = 0

        # Parcurgem toate liniile comenzii.
        for price, qty in zip(prices, quantities):
            # Validare valori individuale.
            if price <= 0 or qty <= 0:
                raise ValueError("Preturile si cantitatile trebuie sa fie strict pozitive.")

            line_total = price * qty

            # Discount de volum pentru cantitate mare.
            if qty >= 10:
                line_total *= 0.95
                bulk_discount_lines += 1

            total += line_total

        # Discount premium daca pragul este atins.
        if is_premium and total >= 500:
            total *= 0.90
        else:
            total *= 1.0

        # Taxa de transport urgent.
        if urgent_shipping:
            total += self.urgent_shipping_fee

        # Discount suplimentar daca exista cel putin 2 linii bulk.
        if bulk_discount_lines >= 2:
            total *= 0.97

        # Aplicare cupon.
        total *= (1 - coupon_percent / 100)

        return round(total, 2)

    def classify_order(self, final_total: float) -> str:
        """
        Clasifica o comanda dupa totalul final.
        """

        if final_total < 0:
            raise ValueError("final_total nu poate fi negativ.")

        if final_total < 200:
            return "small"
        elif final_total <= 500:
            return "medium"
        else:
            return "large"