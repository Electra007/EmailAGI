class DecisionAgent:

    def make_decision(
        self,
        confidence,
        novelty,
        context,
        policy
    ):

        if context is None:

            return {
                "status": "Manual Review",
                "team": "Customer Verification Team"
            }

        if context["kyc_status"] != "Verified":

            return {
                "status": "Pending KYC",
                "team": "Compliance Team"
            }

        if novelty["novel"]:

            return {
                "status": "Manual Review",
                "team": "Innovation Team"
            }

        if confidence["confidence"] > 0.90:

            return {
                "status": "Approved",
                "team": confidence["category"] + " Team"
            }

        return {
            "status": "Manual Review",
            "team": "Support Team"
        }