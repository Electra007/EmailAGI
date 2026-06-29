import joblib
import os

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "classifier.pkl"
)

model = joblib.load(MODEL_PATH)


class EmailClassifier:

    def predict(self, subject, body):

        text = subject + " " + body

        prediction = model.predict([text])[0]

        confidence = model.predict_proba([text]).max()

        return prediction, float(confidence)