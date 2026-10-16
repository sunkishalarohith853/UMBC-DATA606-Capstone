# Crime Probability App

Interactive Streamlit app: enter a crime category, location type, hour, day of week, month,
and year, and get an estimated probability of a crime occurring, with a low / medium / high
risk band.

## Run

From the repository root:

```bash
pip install -r requirements.txt

# one-time: train the model the app loads
python app/train_model.py

# launch
streamlit run app/app.py
```

`train_model.py` builds the labeled dataset (reported crimes as positives + synthetic
negatives sampled from observed feature distributions), trains a
`OneHotEncoder` + `RandomForestClassifier` pipeline, and saves it to
`app/crime_probability_model.pkl` (git-ignored; regenerated locally).
