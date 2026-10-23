"""
Tropical Cafe receipt printer.

Prints one receipt in the same layout as the photo.
Run:  python receipt.py
"""

from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# ---- Settings (from the photo) ----
SHOP_NAME = "Tropical Cafe & Restaurant"
POWERED_BY = "Powered By ATECH"
THANK_YOU = "THANK YOU FOR COMING"
EXCHANGE_RATE = 4100   # riel for 1 USD  (photo: $4.00 = R 16,400)
RIEL_STEP = 100        # riel is rounded to the nearest 100
WIDTH = 42             # width of the receipt in characters


def to_riel(usd):
    """Convert USD to riel and round to the nearest RIEL_STEP."""
    steps = (usd * EXCHANGE_RATE / RIEL_STEP).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return int(steps) * RIEL_STEP


def line(label, value):
    """Make one line with the label on the left and the value on the right."""
    return f"{label:<{WIDTH - len(value)}}{value}"


def build_receipt(queue_no, ticket, table, time_in, items, pax):
    """
    Build the receipt text.
    items: list of (name, size, qty, unit_price as Decimal)
    """
    time_out = datetime.now()
    rule = "-" * WIDTH

    # Calculate the amount for each row and the totals
    rows = [(name, size, qty, price, price * qty) for name, size, qty, price in items]
    total = sum(row[4] for row in rows)
    riel = to_riel(total)

    lines = [
        SHOP_NAME.center(WIDTH),
        f"Queue No : {queue_no}".center(WIDTH),
        "",
        f"{table}   {ticket}".center(WIDTH),
        rule,
        line("Cashier:", "Cashier"),
        line("Table:", table),
        line("Time-In:", f"{time_in:%m/%d/%Y %I:%M %p}"),
        line("Time-Out:", f"{time_out:%m/%d/%Y %I:%M %p}"),
        line("Pax:", str(pax)),
        line("Counter:", "POS Cashier"),
        rule,
        f"{'Description':<16}{'Size':<8}{'Qty':>4}{'Price':>7}{'Amount':>7}",
    ]

    for name, size, qty, price, amount in rows:
        lines.append(f"{name:<16}{size:<8}{qty:>4}{price:>7.2f}{amount:>7.2f}")

    lines += [
        rule,
        line("Sub Total:", f"${total:.2f}"),
        line("Grand Total ($):", f"${total:.2f}"),
        line("Grand Total (R):", f"R {riel:,}"),
        rule,
        THANK_YOU.center(WIDTH),
        POWERED_BY.center(WIDTH),
    ]
    return "\n".join(lines)


def main():
    # The order from the photo
    receipt = build_receipt(
        queue_no=17,
        ticket="T25-28339",
        table="Take-Away-17",
        time_in=datetime.now(),
        pax=1,
        items=[
            ("Iced Cafe Latte", "16oz", 2, Decimal("2.00")),
        ],
    )
    print(receipt)


if __name__ == "__main__":
    main()