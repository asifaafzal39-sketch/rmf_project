import pandas as pd


def calculate_rfm(df):
    """Step 3: Recency, Frequency, Monetary nikalo."""
    # Snapshot date = last transaction date + 1 din
    snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("CustomerID").agg(
        Recency=("InvoiceDate", lambda x: (snapshot_date - x.max()).days),
        Frequency=("InvoiceNo", "nunique"),
        Monetary=("TotalPrice", "sum"),
    ).reset_index()

    return rfm


def add_rfm_scores(rfm):
    """Har metric ko 1-5 score do (5 = best)."""
    rfm = rfm.copy()
    # Recency: kam din = behtar customer, isliye labels ulte
    rfm["R_Score"] = pd.qcut(rfm["Recency"].rank(method="first"), 5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm["M_Score"] = pd.qcut(rfm["Monetary"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm["RFM_Score"] = rfm["R_Score"] + rfm["F_Score"] + rfm["M_Score"]
    return rfm