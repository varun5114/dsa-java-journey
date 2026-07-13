"""
Step 1: Baseline Toxic Comment Classifier
-------------------------------------------
Goal: Train a simple, explainable baseline model (TF-IDF + Logistic Regression)
on the Jigsaw Toxic Comment Classification dataset.

Why start simple?
- Fast to train, easy to explain in interviews ("why did you choose this first?")
- Gives you a working end-to-end pipeline before adding complexity
- Sets a baseline score so you can later prove an upgrade (e.g. DistilBERT) is worth it

HOW TO USE:
1. Download train.csv from the Jigsaw Toxic Comment Classification Challenge (Kaggle)
2. Place it in the same folder as this script, named "train.csv"
3. Run: pip install pandas scikit-learn joblib
4. Run: python train_baseline_model.py
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

# The 6 label categories in the Jigsaw dataset
LABEL_COLUMNS = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]


def load_data(path="train.csv"):
    """Load the Jigsaw dataset."""
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows.")
    return df


def build_pipeline():
    """Create the TF-IDF vectorizer + multi-label logistic regression model."""
    vectorizer = TfidfVectorizer(
        max_features=20000,     # cap vocabulary size for speed/memory
        stop_words="english",
        ngram_range=(1, 2),     # unigrams + bigrams capture more context
    )
    # OneVsRest lets us predict multiple independent labels
    # (a comment can be BOTH toxic AND threat, etc.)
    classifier = OneVsRestClassifier(
        LogisticRegression(max_iter=1000, class_weight="balanced")
    )
    return vectorizer, classifier


def train_and_evaluate(df):
    X = df["comment_text"].fillna("")
    y = df[LABEL_COLUMNS]

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    vectorizer, classifier = build_pipeline()

    print("Vectorizing text...")
    X_train_vec = vectorizer.fit_transform(X_train)
    X_val_vec = vectorizer.transform(X_val)

    print("Training model...")
    classifier.fit(X_train_vec, y_train)

    print("\nEvaluating on validation set...")
    y_pred = classifier.predict(X_val_vec)
    y_pred_proba = classifier.predict_proba(X_val_vec)

    print(classification_report(y_val, y_pred, target_names=LABEL_COLUMNS))

    # ROC-AUC per label - a common metric for this dataset (used in the original Kaggle competition)
    for i, label in enumerate(LABEL_COLUMNS):
        auc = roc_auc_score(y_val[label], y_pred_proba[:, i])
        print(f"{label}: ROC-AUC = {auc:.4f}")

    return vectorizer, classifier


def save_artifacts(vectorizer, classifier, out_dir="."):
    """Save the trained model + vectorizer so the serving layer can load them later."""
    joblib.dump(vectorizer, f"{out_dir}/vectorizer.joblib")
    joblib.dump(classifier, f"{out_dir}/model.joblib")
    print(f"\nSaved vectorizer.joblib and model.joblib to {out_dir}/")


if __name__ == "__main__":
    df = load_data("train.csv")
    vectorizer, classifier = train_and_evaluate(df)
    save_artifacts(vectorizer, classifier)
    print("\nDone! Next step: we'll wrap this model in a small Python inference API.")