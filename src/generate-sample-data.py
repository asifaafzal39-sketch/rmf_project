import numpy as np
import pandas as pd
from config import RAW_DATA_PATH


def generate(n_customers=1500, seed=42):
    rng = np.random.default_rng(seed)
    rows = []
    invoice = 100000
    end_date = pd.Timestamp("2011-12-09")

    for cid in range(12000, 12000 + n_customers):
        kind = rng.choice(["loyal", "new", "churn", "regular"], p=[0.2, 0.2, 0.25, 0.35])
        if kind == "loyal":
            n_orders, last_days = rng.integers(8, 25), rng.integers(1, 30)
        elif kind == "new":
            n_orders, last_days = rng.integers(1, 3), rng.integers(1, 25)
        elif kind == "churn":
            n_orders, last_days = rng.integers(3, 10), rng.integers(150, 360)
        else:
            n_orders, last_days = rng.integers(2, 7), rng.integers(30, 150)

        last_order = end_date - pd.Timedelta(days=int(last_days))
        for _ in range(int(n_orders)):
            invoice += 1
            date = last_order - pd.Timedelta(days=int(rng.integers(0, 300)))
            for _ in range(int(rng.integers(1, 5))):
                rows.append([
                    str(invoice), f"P{rng.integers(1000, 1100)}", "Sample Product",
                    int(rng.integers(1, 12)), date, round(float(rng.uniform(1, 40)), 2),
                    cid, "United Kingdom",
                ])

    df = pd.DataFrame(rows, columns=["InvoiceNo", "StockCode", "Description",
                                     "Quantity", "InvoiceDate", "UnitPrice",
                                     "CustomerID", "Country"])
    df.loc[df.sample(frac=0.02, random_state=1).index, "CustomerID"] = np.nan
    cancel_idx = df.sample(frac=0.01, random_state=2).index
    df.loc[cancel_idx, "InvoiceNo"] = "C" + df.loc[cancel_idx, "InvoiceNo"]
    df.to_csv(RAW_DATA_PATH, index=False)
    print(f"Sample data saved: {RAW_DATA_PATH}  ({len(df)} rows)")


if __name__ == "__main__":
    generate()