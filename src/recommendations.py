RECOMMENDATIONS = {
    "Loyal": "Offer a VIP/loyalty program, early access and exclusive discounts, and add a referral bonus.",
    "New": "Send a welcome email series, offer a discount on the second purchase and share product guides.",
    "Churn Risk": "Run a 'We miss you' campaign, give a personalized discount coupon and send a feedback survey.",
    "Lost": "Send a low-cost win-back email/SMS, try one big discount offer, then stop spending budget on them.",
    "Potential": "Cross-sell and upsell, offer bundle deals and send reminders to increase purchase frequency.",
}


def print_recommendations(summary):
    print("\n=== Targeted Marketing Recommendations ===")
    for segment in summary.index:
        print(f"\n[{segment}] -> {RECOMMENDATIONS.get(segment, '')}")