import numpy as np


def assign_segments(rfm):
    """Step 4: Customers ko groups mein baanto."""
    r, f = rfm["R_Score"], rfm["F_Score"]

    conditions = [
        (r >= 3) & (f >= 4),   # Recent bhi, frequent bhi
        (r >= 4) & (f <= 2),   # Abhi abhi aaye, kam orders
        (r <= 2) & (f >= 3),   # Pehle acha kharidte the, ab gayab
        (r <= 2) & (f <= 2),   # Purane aur kam active
    ]
    labels = ["Loyal", "New", "Churn Risk", "Lost"]

    rfm = rfm.copy()
    rfm["Segment"] = np.select(conditions, labels, default="Potential")
    return rfm