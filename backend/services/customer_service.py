import pandas as pd
import random
from faker import Faker
import os

fake = Faker("en_IN")

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

KYC_STATUS = [
    "Verified",
    "Pending",
    "Expired"
]


def generate_customers(records=10000):

    customers = []

    # -------------------------
    # GUARANTEED UNIQUE IDs
    # -------------------------

    customer_ids = list(range(100000, 100000 + records))
    random.shuffle(customer_ids)

    for i in range(records):

        customers.append({

            "customer_id": customer_ids[i],

            "customer_name": fake.name(),

            "account_type": random.choice(ACCOUNT_TYPES),

            "customer_tier": random.choice(CUSTOMER_TIERS),

            "risk_score": round(random.uniform(0, 1), 2),

            "complaint_history": random.randint(0, 10),

            "kyc_status": random.choice(KYC_STATUS),

            "years_with_bank": random.randint(1, 25)

        })

    df = pd.DataFrame(customers)

    os.makedirs("synthetic_data", exist_ok=True)

    output_file = "synthetic_data/customers.csv"

    df.to_csv(output_file, index=False)

    print("=" * 60)
    print(df.head())
    print("=" * 60)

    print("\nCustomer Dataset Generated Successfully!")
    print("Customers :", len(df))
    print("Unique Customer IDs :", df["customer_id"].nunique())
    print("Duplicates :", len(df) - df["customer_id"].nunique())
    print("Saved to :", output_file)


if __name__ == "__main__":
    generate_customers()