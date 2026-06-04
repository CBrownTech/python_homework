import sqlite3
from pathlib import Path

import pandas as pd

DB_PATH = Path(__file__).resolve().parent.parent / "db" / "lesson.db"
OUTPUT_PATH = Path(__file__).resolve().parent / "order_summary.csv"

QUERY = """
    SELECT line_items.line_item_id, line_items.quantity,
           products.product_id, products.product_name, products.price
    FROM line_items
    JOIN products ON line_items.product_id = products.product_id
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql(QUERY, conn)

print("Line items with products (first 5 rows):")
print(df.head())

df["total"] = df["quantity"] * df["price"]

print("\nWith total column (first 5 rows):")
print(df.head())

summary = (
    df.groupby("product_id")
    .agg(
        line_item_id=("line_item_id", "count"),
        total=("total", "sum"),
        product_name=("product_name", "first"),
    )
    .reset_index()
)

print("\nOrder summary by product (first 5 rows):")
print(summary.head())

summary = summary.sort_values("product_name")

summary.to_csv(OUTPUT_PATH, index=False)
print(f"\nWrote {OUTPUT_PATH}")
