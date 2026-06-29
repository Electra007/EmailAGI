from backend.database.db import SessionLocal
from backend.database.models import Customer


class ContextAgent:

    def __init__(self):
        self.session = SessionLocal()

    def lookup(self, email):

        customer_id = email["customer_id"]

        customer = (
            self.session.query(Customer)
            .filter(Customer.customer_id == customer_id)
            .first()
        )

        if customer is None:

            print("[Context Agent] Customer Not Found")

            return None

        print("[Context Agent] Customer Found")

        return {

            "customer_id": customer.customer_id,

            "customer_name": customer.customer_name,

            "tier": customer.customer_tier,

            "account_type": customer.account_type,

            "risk_score": customer.risk_score,

            "complaint_history": customer.complaint_history,

            "kyc_status": customer.kyc_status

        }