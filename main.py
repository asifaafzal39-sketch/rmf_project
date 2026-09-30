import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from config import RAW_DATA_PATH, PROCESSED_DIR
from data_cleaning import load_data, clean_data
from rfm_calculation import calculate_rfm, add_rfm_scores
from segmentation import assign_segments
from analysis import segment_summary
from recommendations import print_recommendations
from visualization import plot_all


def main():
    # Agar dataset nahi mila to sample data bana do
    if not RAW_DATA_PATH.exists():
        print("Dataset nahi mila, sample data ban raha hai...")
        from generate_sample_data import generate
        generate()

    df = load_data()                    # Step 1
    df = clean_data(df)                 # Step 2
    rfm = calculate_rfm(df)             # Step 3
    rfm = add_rfm_scores(rfm)
    rfm = assign_segments(rfm)          # Step 4
    summary = segment_summary(rfm)      # Step 5

    print("\n=== Segment Summary ===")
    print(summary.to_string())

    print_recommendations(summary)      # Step 6
    plot_all(rfm, summary)              # Step 7

    rfm.to_csv(PROCESSED_DIR / "rfm_segments.csv", index=False)
    summary.to_csv(PROCESSED_DIR / "segment_summary.csv")
    print("\nDone! Results data/processed/ aur outputs/ mein hain.")


if __name__ == "__main__":
    main()