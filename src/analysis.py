def segment_summary(rfm):
    """Step 5: Har segment ka behavior analyze karo."""
    summary = rfm.groupby("Segment").agg(
        Customers=("CustomerID", "count"),
        Avg_Recency=("Recency", "mean"),
        Avg_Frequency=("Frequency", "mean"),
        Avg_Monetary=("Monetary", "mean"),
        Total_Revenue=("Monetary", "sum"),
    ).round(2)

    summary["Customer_%"] = (summary["Customers"] / summary["Customers"].sum() * 100).round(1)
    summary["Revenue_%"] = (summary["Total_Revenue"] / summary["Total_Revenue"].sum() * 100).round(1)
    return summary.sort_values("Total_Revenue", ascending=False)