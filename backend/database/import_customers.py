import pandas as pd

from backend.database.db import SessionLocal
from backend.database.models import Customer

session = SessionLocal()

print("Reading customer dataset...")

df = pd.read_csv("synthetic_data/customers.csv")

print(f"Total rows in CSV: {len(df)}")
print(f"Unique customer IDs: {df['customer_id'].nunique()}")

# Check duplicates before importing
duplicates = df[df.duplicated(subset=["customer_id"], keep=False)]

if not duplicates.empty:
    print("\nERROR: Duplicate customer IDs found in CSV!")
    print(duplicates.head())
    session.close()
    raise SystemExit("Fix customer_service.py or regenerate customers.csv.")

print("Clearing existing customer table...")

session.query(Customer).delete()
session.commit()

print("Importing customers...")

for _, row in df.iterrows():

    customer = Customer(
        customer_id=int(row["customer_id"]),
        customer_name=row["customer_name"],
        account_type=row["account_type"],
        customer_tier=row["customer_tier"],
        risk_score=float(row["risk_score"]),
        complaint_history=int(row["complaint_history"]),
        kyc_status=row["kyc_status"]
    )

    session.add(customer)

session.commit()

print("\n✅ Import Successful!")
print(f"Customers Imported: {len(df)}")

session.close()