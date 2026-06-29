import pandas as pd
import random
from faker import Faker
import uuid
import os

fake = Faker("en_IN")

# ------------------------------------
# Complaint Categories
# ------------------------------------

CATEGORIES = {
    "Credit Card": [
        "Card charged twice",
        "Credit card not delivered",
        "Credit card blocked",
        "Credit limit not updated",
        "Unable to pay credit card bill"
    ],

    "Loan": [
        "Loan EMI deducted twice",
        "Need foreclosure letter",
        "Home loan interest mismatch",
        "Loan not approved",
        "Personal loan status"
    ],

    "Fraud": [
        "Unauthorized transaction",
        "Debit card stolen",
        "UPI fraud",
        "Phishing complaint",
        "OTP fraud"
    ],

    "Savings Account": [
        "Account frozen",
        "Passbook issue",
        "Statement required",
        "Interest not credited",
        "Minimum balance penalty"
    ],

    "Internet Banking": [
        "Cannot login",
        "Password reset",
        "Server error",
        "Session timeout",
        "Internet banking blocked"
    ],

    "UPI": [
        "Money debited not received",
        "UPI pending",
        "Wrong beneficiary",
        "QR payment failed",
        "UPI registration failed"
    ],

    "Debit Card": [
        "Card damaged",
        "ATM cash not dispensed",
        "PIN generation issue",
        "Card expired",
        "International transaction failed"
    ]
}

PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

ACCOUNT_TYPES = [
    "Savings",
    "Current",
    "Salary",
    "NRI"
]

CUSTOMER_TIERS = [
    "Regular",
    "Silver",
    "Gold",
    "Platinum",
    "Wealth"
]


# ------------------------------------
# Generate Email
# ------------------------------------

def generate_email(category):

    subject = random.choice(CATEGORIES[category])

    body = f"""
Dear ICICI Bank,

{subject}.

I am facing this issue since the last few days.

Kindly resolve this issue as soon as possible.

Customer Name:
{fake.name()}

Account Number:
XXXX{random.randint(1000,9999)}

Regards,

{fake.name()}
"""

    return subject, body


# ------------------------------------
# Generate Dataset
# ------------------------------------

def generate_dataset(records=25000):

    data = []

    # Generate UNIQUE customer IDs
    customer_ids = list(range(100000, 100000 + records))
    random.shuffle(customer_ids)

    for i in range(records):

        category = random.choice(list(CATEGORIES.keys()))

        subject, body = generate_email(category)

        data.append({

            "email_id": str(uuid.uuid4()),

            "customer_id": customer_ids[i],

            "customer_name": fake.name(),

            "customer_tier": random.choice(CUSTOMER_TIERS),

            "account_type": random.choice(ACCOUNT_TYPES),

            "priority": random.choice(PRIORITIES),

            "category": category,

            "subject": subject,

            "body": body,

            "timestamp": fake.date_time_between(
                start_date="-365d",
                end_date="now"
            )

        })

    df = pd.DataFrame(data)

    os.makedirs("synthetic_data", exist_ok=True)

    output_path = "synthetic_data/banking_emails.csv"

    df.to_csv(
        output_path,
        index=False
    )

    print("=" * 50)
    print(df.head())
    print("=" * 50)
    print(f"\nDataset Generated Successfully!")
    print(f"Total Emails : {len(df)}")
    print(f"Unique Customer IDs : {df['customer_id'].nunique()}")
    print(f"Dataset Saved At : {output_path}")


# ------------------------------------
# Main
# ------------------------------------

if __name__ == "__main__":
    generate_dataset()