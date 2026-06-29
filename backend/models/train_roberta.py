import pandas as pd
from sklearn.preprocessing import LabelEncoder

from datasets import Dataset

from transformers import (
    RobertaTokenizer,
    RobertaForSequenceClassification,
    TrainingArguments,
    Trainer
)

# Load datasets
train = pd.read_csv("synthetic_data/splits/train.csv")
validation = pd.read_csv("synthetic_data/splits/validation.csv")

# Encode labels
encoder = LabelEncoder()

train["label"] = encoder.fit_transform(train["category"])
validation["label"] = encoder.transform(validation["category"])

train_dataset = Dataset.from_pandas(
    train[["text", "label"]]
)

validation_dataset = Dataset.from_pandas(
    validation[["text", "label"]]
)

tokenizer = RobertaTokenizer.from_pretrained("roberta-base")


def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        padding="max_length",
        max_length=128
    )


train_dataset = train_dataset.map(tokenize, batched=True)
validation_dataset = validation_dataset.map(tokenize, batched=True)

model = RobertaForSequenceClassification.from_pretrained(
    "roberta-base",
    num_labels=len(encoder.classes_)
)

training_args = TrainingArguments(
    output_dir="./roberta_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_steps=50
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=validation_dataset
)

trainer.train()

model.save_pretrained("backend/models/roberta_model")

tokenizer.save_pretrained("backend/models/roberta_model")

print("Training Complete!")