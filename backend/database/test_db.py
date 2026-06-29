from backend.database.db import SessionLocal
from backend.database.models import Customer

session = SessionLocal()

print("=" * 40)
print("DATABASE TEST")
print("=" * 40)

print("Total Customers:", session.query(Customer).count())

customer = session.query(Customer).first()

print("\nFirst Customer:")

if customer:
    print("Customer ID:", customer.customer_id)
    print("Name:", customer.customer_name)
    print("Tier:", customer.customer_tier)
else:
    print("No customer found!")

session.close()