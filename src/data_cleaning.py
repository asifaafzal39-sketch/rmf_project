import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DIR


def load_data(path=RAW_DATA_PATH):
    """Step 1: CSV file load karo."""
    df = pd.read_csv(path, encoding="ISO-8859-1")
    print(f"Raw data shape: {df.shape}")
    return df


def clean_data(df):
    """Step 2: Data clean karo."""
    df = df.copy()

    # Missing CustomerID wali rows hatao (segmentation customer par hoti hai)
    df = df.dropna(subset=["CustomerID"])

    # Duplicate rows hatao
    df = df.drop_duplicates()

    # Cancelled orders (InvoiceNo 'C' se start hota hai) hatao
    df["InvoiceNo"] = df["InvoiceNo"].astype(str)
    df = df[~df["InvoiceNo"].str.startswith("C")]

    # Negative / zero quantity aur price hatao
    df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

    # Data types theek karo
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["CustomerID"] = df["CustomerID"].astype(int)

    # Har row ki total value
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    print(f"Clean data shape: {df.shape}")
    df.to_csv(PROCESSED_DIR / "clean_data.csv", index=False)
    return df