from backend.models.classifier import EmailClassifier


class ConfidenceAgent:

    def __init__(self):
        self.model = EmailClassifier()

    def check(self, email):

        prediction, confidence = self.model.predict(
            email["subject"],
            email["body"]
        )

        print(f"[Confidence Agent] Predicted Category : {prediction}")
        print(f"[Confidence Agent] Confidence Score : {confidence:.2f}")

        return {
            "category": prediction,
            "confidence": confidence
        }