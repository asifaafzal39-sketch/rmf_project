import matplotlib
matplotlib.use("Agg")  # Charts file mein save honge
import matplotlib.pyplot as plt
import seaborn as sns
from config import OUTPUT_DIR

sns.set_theme(style="whitegrid")


def plot_all(rfm, summary):
    """Step 7: Charts banao aur outputs/ folder mein save karo."""

    # 1) Har segment mein customers
    plt.figure(figsize=(8, 5))
    sns.barplot(x=summary.index, y=summary["Customers"], hue=summary.index, palette="viridis", legend=False)
    plt.title("Customers per Segment")
    plt.ylabel("Number of Customers")
    plt.savefig(OUTPUT_DIR / "01_customers_per_segment.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 2) Har segment ka revenue share
    plt.figure(figsize=(7, 7))
    plt.pie(summary["Total_Revenue"], labels=summary.index, autopct="%1.1f%%", startangle=90)
    plt.title("Revenue Share by Segment")
    plt.savefig(OUTPUT_DIR / "02_revenue_share.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 3) Recency vs Monetary scatter
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=rfm, x="Recency", y="Monetary", hue="Segment", alpha=0.7)
    plt.title("Recency vs Monetary by Segment")
    plt.savefig(OUTPUT_DIR / "03_recency_vs_monetary.png", dpi=150, bbox_inches="tight")
    plt.close()

    # 4) Average RFM heatmap
    plt.figure(figsize=(8, 5))
    sns.heatmap(summary[["Avg_Recency", "Avg_Frequency", "Avg_Monetary"]],
                annot=True, fmt=".1f", cmap="YlGnBu")
    plt.title("Average RFM per Segment")
    plt.savefig(OUTPUT_DIR / "04_rfm_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Charts saved in: {OUTPUT_DIR}")