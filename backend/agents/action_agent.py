import uuid


class ActionAgent:

    def execute(self, decision):

        print("[Action Agent] Ticket Created")

        return {
            "ticket_id": str(uuid.uuid4()),
            "status": decision["status"],
            "assigned_team": decision["team"]
        }