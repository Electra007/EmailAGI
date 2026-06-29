from pprint import pprint

from backend.utils.logger import logger
from backend.agents.confidence_agent import ConfidenceAgent
from backend.agents.novelty_agent import NoveltyAgent
from backend.agents.context_agent import ContextAgent
from backend.agents.policy_agent import PolicyAgent
from backend.agents.decision_agent import DecisionAgent
from backend.agents.action_agent import ActionAgent


class AgentOrchestrator:

    def __init__(self):
        self.confidence = ConfidenceAgent()
        self.novelty = NoveltyAgent()
        self.context = ContextAgent()
        self.policy = PolicyAgent()
        self.decision = DecisionAgent()
        self.action = ActionAgent()

    def process_email(self, email):

        print("\n==============================")
        print("Running Agentic AI Pipeline...")
        print("==============================\n")

        # Step 1 - Confidence Agent
        confidence = self.confidence.check(email)

        # Step 2 - Novelty Agent
        novelty = self.novelty.check(email)

        # Step 3 - Context Agent
        context = self.context.lookup(email)

        # Step 4 - Policy Agent
        policy = self.policy.evaluate(email)

        # Step 5 - Decision Agent
        decision = self.decision.make_decision(
            confidence,
            novelty,
            context,
            policy
        )

        # Step 6 - Action Agent
        action = self.action.execute(decision)

        # Logging
        logger.info(
            f"""
Customer ID : {email['customer_id']}
Subject     : {email['subject']}
Prediction  : {confidence['category']}
Confidence  : {confidence['confidence']:.2f}
Novelty     : {novelty['novel']}
Similarity  : {novelty['similarity']:.2f}
Decision    : {decision['status']}
Assigned    : {action['assigned_team']}
Ticket ID   : {action['ticket_id']}
"""
        )

        # Return complete pipeline output
        return {
            "ticket": action,
            "confidence": confidence,
            "novelty": novelty,
            "customer": context,
            "policy": policy,
            "decision": decision
        }


if __name__ == "__main__":

    orchestrator = AgentOrchestrator()

    sample_email = {
        "customer_id": 100000,
        "subject": "Card Charged Twice",
        "body": "My card was charged twice yesterday."
    }

    result = orchestrator.process_email(sample_email)

    print("\n================ FINAL OUTPUT ================\n")

    pprint(result)

    print("\n==============================================")