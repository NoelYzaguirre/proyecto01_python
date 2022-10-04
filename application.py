import random
import datetime
from typing import List, Dict
from config import SEAT_ECONOMY, SEAT_PREMIUM, IGV_PERCENT, PRICE_SEAT_PREMIUM, PRICE_SEAT_ECONOMY_TO_LIMA, PRICE_SEAT_ECONOMY_FROM_LIMA, HOLYDAYS, CURRENCY_SYMBOL


def main():

    # Lista de rutas

    tickets: List[Dict[str, str | float | int]] = [
        {
            "code": "LIM - AYA",
            "name": "Lima - Ayacucho",
            "base_price": 55.19,
            "price_seat_economy": PRICE_SEAT_ECONOMY_FROM_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "LIM - CUS",
            "name": "Lima - Cusco",
            "base_price": 136.51,
            "price_seat_economy": PRICE_SEAT_ECONOMY_FROM_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "LIM - ARE",
            "name": "Lima - Arequipa",
            "base_price": 90.59,
            "price_seat_economy": PRICE_SEAT_ECONOMY_FROM_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "LIM - TAR",
            "name": "Lima - Tarapoto",
            "base_price": 71.89,
            "price_seat_economy": PRICE_SEAT_ECONOMY_FROM_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "AYA - LIM",
            "name": "Ayacucho - Lima",
            "base_price": 40.42,
            "price_seat_economy": PRICE_SEAT_ECONOMY_TO_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "CUS - LIM",
            "name": "Cusco - Lima",
            "base_price": 124.32,
            "price_seat_economy": PRICE_SEAT_ECONOMY_TO_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "ARE - LIM",
            "name": "Arequipa - Lima",
            "base_price": 86.59,
            "price_seat_economy": PRICE_SEAT_ECONOMY_TO_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM},
        {
            "code": "TAR - LIM",
            "name": "Tarapoto - Lima",
            "airplane": "A004",
            "base_price": 68.42,
            "price_seat_economy": PRICE_SEAT_ECONOMY_TO_LIMA,
            "price_seat_premium": PRICE_SEAT_PREMIUM}
    ]

    routes: List[Dict[str, str | int]] = [
        {
            "code": "LIM - AYA",
            "name": "Lima - Ayacucho",
            "airplane": "A001",
            "min_sale_ticket_economy": 120,
            "max_sale_ticket_economy": 130,
            "min_sale_ticket_premium": 10,
            "max_sale_ticket_premium": 20,
        },
        {
            "code": "LIM - CUS",
            "name": "Lima - Cusco",
            "airplane": "A002",
            "min_sale_ticket_economy": 130,
            "max_sale_ticket_economy": 144,
            "min_sale_ticket_premium": 15,
            "max_sale_ticket_premium": 24,
        },
        {
            "code": "LIM - ARE",
            "name": "Lima - Arequipa",
            "airplane": "A003",
            "min_sale_ticket_economy": 115,
            "max_sale_ticket_economy": 138,
            "min_sale_ticket_premium": 16,
            "max_sale_ticket_premium": 22,
        },
        {
            "code": "LIM - TAR",
            "name": "Lima - Tarapoto",
            "airplane": "A004",
            "min_sale_ticket_economy": 100,
            "max_sale_ticket_economy": 120,
            "min_sale_ticket_premium": 12,
            "max_sale_ticket_premium": 18,
        },
        {
            "code": "AYA - LIM",
            "name": "Ayacucho - Lima",
            "airplane": "A001",
            "min_sale_ticket_economy": 100,
            "max_sale_ticket_economy": 115,
            "min_sale_ticket_premium": 10,
            "max_sale_ticket_premium": 15,
        },
        {
            "code": "CUS - LIM",
            "name": "Cusco - Lima",
            "airplane": "A002",
            "min_sale_ticket_economy": 105,
            "max_sale_ticket_economy": 120,
            "min_sale_ticket_premium": 14,
            "max_sale_ticket_premium": 20,
        },
        {
            "code": "ARE - LIM",
            "name": "Arequipa - Lima",
            "airplane": "A003",
            "min_sale_ticket_economy": 100,
            "max_sale_ticket_economy": 110,
            "min_sale_ticket_premium": 13,
            "max_sale_ticket_premium": 28,
        },
        {
            "code": "TAR - LIM",
            "name": "Tarapoto - Lima",
            "airplane": "A004",
            "min_sale_ticket_economy": 90,
            "max_sale_ticket_economy": 105,
            "min_sale_ticket_premium": 10,
            "max_sale_ticket_premium": 15,
        }

    ]

    start = datetime.date(2022, 1, 1)
    periods = 365
    date_range = []

    for day in range(periods):
        date = (start + datetime.timedelta(days=day)).isoformat()
        date_range.append(date)

    # inicializamos la lista donde guardaran los tickets
    list_tickets: List[Dict[str, str | float | int]] = []

    # Recorremos todos los dias para generar las ventas alatorias de pasajes
    for d in date_range:
        # variable para almacenar los ingresos por las venta de tickets economicos
        sales_economy: float = 0

        # variable para almacenar el total de tickets economicos
        total_ticket_economy: int = 0

        # variable para almacenar los ingresos por las venta de tickets premium
        sales_premium: float = 0

        # variable para almacenar el total de tickets premium
        total_ticket_premium: int = 0

        # variable para almacenar los importes de IGV
        igv_mount: float = 0

        for k, v in enumerate(routes):
            # Obtenemos el total de ventas de pasajes economicos y premium de manera aleatoria
            sales_ticket_economy: int = random.randint(
                int(v["min_sale_ticket_economy"]), int(v["max_sale_ticket_economy"]))

            total_ticket_economy += sales_ticket_economy

            sales_ticket_premium: int = random.randint(
                int(v["min_sale_ticket_premium"]), int(v["max_sale_ticket_premium"]))

            total_ticket_premium += sales_ticket_premium

            # guardamos el nombre de la ruta y del avion
            name_route: str = v["name"]
            name_airplane: str = v["airplane"]

            # obtenemos el precio base y precio adicional por tipo de asiento
            price_seat_economy: float = float(tickets[k]['price_seat_economy'])
            price_seat_premium: float = float(tickets[k]['price_seat_premium'])
            base_price: float = float(tickets[k]['base_price'])

            # generamos los tickes economicos y calculando el precio adicional si es un dia feriado
            for s in range(sales_ticket_economy):
                ticket_subtotal_economy: float = base_price + \
                    price_seat_economy if day in HOLYDAYS else base_price

                ticket_igv_economy: float = round(
                    ticket_subtotal_economy*IGV_PERCENT/100, 2)
                ticket_total_economy: float = round(
                    ticket_subtotal_economy + ticket_igv_economy, 2)

                sales_economy += ticket_total_economy

                igv_mount += ticket_igv_economy

                ticket_economy: Dict[str, str | float | int] = {
                    "route": name_route,
                    "airplane": name_airplane,
                    "subtotal": ticket_subtotal_economy,
                    "igv": ticket_igv_economy,
                    "total": ticket_total_economy,
                    "date": d
                }

                list_tickets.append(ticket_economy)

            # generamos los tickes premium y calculando el precio adicional si es un dia feriado
            for s in range(sales_ticket_premium):
                ticket_subtotal_premium: float = base_price + \
                    price_seat_premium if day in HOLYDAYS else base_price

                ticket_igv_premium: float = round(
                    ticket_subtotal_premium*IGV_PERCENT/100, 2)
                ticket_total_premium: float = round(
                    ticket_subtotal_premium + ticket_igv_premium, 2)

                sales_premium += ticket_total_premium

                igv_mount += ticket_igv_premium

                ticket_premium: Dict[str, str | float] = {
                    "route": name_route,
                    "airplane": name_airplane,
                    "subtotal": ticket_subtotal_premium,
                    "igv": ticket_igv_premium,
                    "total": ticket_total_premium,
                    "date": d
                }

                list_tickets.append(ticket_premium)

    # Calculando el valor promedio de un pasaeje economico
    ticket_economy_avg: float = round(sales_economy / total_ticket_economy, 2)

    # Calculando el valor promedio de un pasaeje premium
    ticket_premium_avg: float = round(sales_premium / total_ticket_premium, 2)

    # Aplicando formato de moneda a la variable sales_economy,sales_premium y igv_mount
    display_total_sales_economy: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, sales_economy)
    display_total_sales_premium: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, sales_premium)
    display_total_igv: str = "{}{:,.2f}".format(CURRENCY_SYMBOL, igv_mount)
    display_avg_ticket_economy: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, ticket_economy_avg)
    display_avg_ticket_premium: str = "{}{:,.2f}".format(
        CURRENCY_SYMBOL, ticket_premium_avg)

    print("¿Cuál es el total de pasajes vendidos entre todos los vuelos?",
          len(list_tickets), sep="\n")
    print("¿Cuál es el total de ingresos por la venta de pasajes económicos?",
          display_total_sales_economy, sep="\n")
    print("¿Cuál es el total de ingresos por la venta de pasajes premium?",
          display_total_sales_premium, sep="\n")
    print("¿Cuál es el importe total de IGV cobrado?",
          display_total_igv, sep="\n")
    print("¿Cuál es el valor promedio de un pasaje económico?",
          display_avg_ticket_economy, sep="\n")
    print("¿Cuál es el valor promedio de un pasaje premium?",
          display_avg_ticket_premium, sep="\n")


if __name__ == "__main__":
    main()
