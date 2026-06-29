import pandas as pd
from sklearn.model_selection import train_test_split
import os


class DatasetPreparer:

    def __init__(self):

        self.input_file = "synthetic_data/banking_emails.csv"

    def prepare(self):

        df = pd.read_csv(self.input_file)

        df["text"] = df["subject"] + " " + df["body"]

        df = df[["text", "category"]]

        train, temp = train_test_split(
            df,
            test_size=0.2,
            random_state=42,
            stratify=df["category"]
        )

        validation, test = train_test_split(
            temp,
            test_size=0.5,
            random_state=42,
            stratify=temp["category"]
        )

        os.makedirs("synthetic_data/splits", exist_ok=True)

        train.to_csv("synthetic_data/splits/train.csv", index=False)

        validation.to_csv("synthetic_data/splits/validation.csv", index=False)

        test.to_csv("synthetic_data/splits/test.csv", index=False)

        print("Training:", len(train))
        print("Validation:", len(validation))
        print("Testing:", len(test))


if __name__ == "__main__":

    DatasetPreparer().prepare()