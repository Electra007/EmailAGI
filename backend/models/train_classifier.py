import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ============================================================
# Configuration
# ============================================================

DATASET_PATH = "synthetic_data/banking_emails.csv"
MODEL_DIR = "backend/models"

os.makedirs(MODEL_DIR, exist_ok=True)

# ============================================================
# Load Dataset
# ============================================================

print("=" * 70)
print("LOADING DATASET")
print("=" * 70)

df = pd.read_csv(DATASET_PATH)

print(f"Dataset Loaded Successfully")
print(f"Total Emails      : {len(df)}")
print(f"Unique Categories : {df['category'].nunique()}")

# Combine subject and body

df["text"] = (
    df["subject"].fillna("") +
    " " +
    df["body"].fillna("")
)

X = df["text"]
y = df["category"]

# ============================================================
# Train/Test Split
# ============================================================

print("\nSplitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# ============================================================
# Build ML Pipeline
# ============================================================

print("\nBuilding ML Pipeline...")

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            stop_words="english",
            max_features=5000,
            ngram_range=(1, 2)
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=1000,
            random_state=42
        )
    )
])

# ============================================================
# Train Model
# ============================================================

print("\nTraining Model...")

model.fit(X_train, y_train)

print("Training Complete!")

# ============================================================
# Evaluate
# ============================================================

print("\nEvaluating Model...")

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n" + "=" * 70)
print("MODEL PERFORMANCE")
print("=" * 70)

print(f"Accuracy : {accuracy:.4f}")

print("\nClassification Report\n")

report = classification_report(
    y_test,
    predictions
)

print(report)

# ============================================================
# Save Accuracy
# ============================================================

with open(
    os.path.join(MODEL_DIR, "accuracy.txt"),
    "w"
) as f:

    f.write(f"{accuracy:.4f}")

# ============================================================
# Save Model
# ============================================================

joblib.dump(
    model,
    os.path.join(
        MODEL_DIR,
        "classifier.pkl"
    )
)

joblib.dump(
    model.classes_,
    os.path.join(
        MODEL_DIR,
        "classes.pkl"
    )
)

print("\nModel Saved Successfully!")

# ============================================================
# Confusion Matrix
# ============================================================

print("\nGenerating Confusion Matrix...")

cm = confusion_matrix(
    y_test,
    predictions,
    labels=model.classes_
)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

fig, ax = plt.subplots(figsize=(10, 8))

disp.plot(
    ax=ax,
    xticks_rotation=45,
    colorbar=False
)

plt.title("Email Classification Confusion Matrix")
plt.tight_layout()

plt.savefig(
    os.path.join(
        MODEL_DIR,
        "confusion_matrix.png"
    )
)

plt.close()

print("Confusion Matrix Saved!")

# ============================================================
# Final Summary
# ============================================================

print("\n" + "=" * 70)
print("TRAINING COMPLETED SUCCESSFULLY")
print("=" * 70)

print(f"Dataset Used        : {DATASET_PATH}")
print(f"Model Accuracy      : {accuracy:.4f}")
print(f"Model Saved         : {MODEL_DIR}/classifier.pkl")
print(f"Classes Saved       : {MODEL_DIR}/classes.pkl")
print(f"Accuracy File       : {MODEL_DIR}/accuracy.txt")
print(f"Confusion Matrix    : {MODEL_DIR}/confusion_matrix.png")

print("=" * 70)