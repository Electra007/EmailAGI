class PolicyAgent:

    def __init__(self):
        pass

    def evaluate(self,email):

        policy = {

            "sla":"2 Hours",

            "priority":"High"

        }

        print("[Policy Agent] Policy Loaded")

        return policy