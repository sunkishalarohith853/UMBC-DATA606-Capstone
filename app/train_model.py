"""Train the crime-probability model used by the Streamlit app.

Reads data/chicago_crimes_2019_2025.csv, builds a labeled dataset with
synthetic negative sampling (each reported crime is a positive example;
negatives are random feature combinations drawn from the observed value
distributions), trains a scikit-learn pipeline, and saves it to
app/crime_probability_model.pkl.

Run from the repo root:
    python app/train_model.py
Then launch the app:
    streamlit run app/app.py
"""

from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

APP_DIR = Path(__file__).resolve().parent
ROOT = APP_DIR.parent
DATA_PATH = ROOT / "data" / "chicago_crimes_2019_2025.csv"
MODEL_PATH = APP_DIR / "crime_probability_model.pkl"

FEATURES = ["primary_type", "location_description", "hour", "day_of_week", "month", "year"]
TARGET = "crime"


def load_positives() -> pd.DataFrame:
    """Each reported crime becomes a positive example (crime = 1)."""
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["hour"] = df["date"].dt.hour
    df["day_of_week"] = df["date"].dt.day_name()
    df["month"] = df["date"].dt.month
    positives = df[FEATURES].dropna().copy()
    positives[TARGET] = 1
    return positives


def make_negatives(positives: pd.DataFrame, seed: int = 42) -> pd.DataFrame:
    """Synthetic negatives: random feature combos from observed distributions,
    resampled until none exactly match a real crime record."""
    rng = np.random.default_rng(seed)
    n = len(positives)
    negatives = pd.DataFrame(
        {c: rng.choice(positives[c].dropna().unique(), size=n) for c in FEATURES}
    )
    positive_tuples = set(map(tuple, positives[FEATURES].astype(str).values))
    while True:
        mask = negatives[FEATURES].astype(str).agg(tuple, axis=1).isin(positive_tuples)
        if not mask.any():
            break
        for c in FEATURES:
            negatives.loc[mask, c] = rng.choice(
                positives[c].dropna().unique(), size=int(mask.sum())
            )
    negatives[TARGET] = 0
    return negatives


def build_pipeline() -> Pipeline:
    categorical = ["primary_type", "location_description", "day_of_week"]
    numeric = ["hour", "month", "year"]
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical),
            ("num", "passthrough", numeric),
        ]
    )
    return Pipeline(
        steps=[
            ("preprocess", preprocessor),
            (
                "model",
                RandomForestClassifier(
                    n_estimators=200, max_depth=20, random_state=42, n_jobs=-1
                ),
            ),
        ]
    )


def main() -> None:
    positives = load_positives()
    negatives = make_negatives(positives)
    data = pd.concat([positives, negatives], ignore_index=True).sample(
        frac=1.0, random_state=42
    )
    X, y = data[FEATURES], data[TARGET]
    print(f"Training rows: {len(data)} "
          f"({int(y.sum())} positives, {int((1 - y).sum())} negatives)")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    proba = pipeline.predict_proba(X_test)[:, 1]
    print(f"Holdout ROC-AUC: {roc_auc_score(y_test, proba):.3f}")
    print(classification_report(y_test, pipeline.predict(X_test)))

    joblib.dump(pipeline, MODEL_PATH)
    print(f"Saved model -> {MODEL_PATH}")


if __name__ == "__main__":
    main()
