class NoveltyAgent:

    def __init__(self):
        print("[Novelty Agent] Initialized")

    def check(self, email):

        text = (
            email.get("subject", "") + " " +
            email.get("body", "")
        ).lower()

        common_phrases = [
            "card charged twice",
            "credit card",
            "loan",
            "fraud",
            "upi",
            "account frozen",
            "statement required",
            "internet banking",
            "password reset",
            "atm cash",
            "pin generation",
            "money debited",
            "payment failed",
            "credit limit",
            "loan emi"
        ]

        novel = True

        for phrase in common_phrases:
            if phrase in text:
                novel = False
                break

        similarity = 0.95 if not novel else 0.30

        print(f"[Novelty Agent] Novel = {novel}")
        print(f"[Novelty Agent] Similarity = {similarity:.2f}")

        return {
            "novel": novel,
            "similarity": similarity
        }