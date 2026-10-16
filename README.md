# Chicago Crime Prediction — UMBC DATA 606 Capstone

Predicting crime occurrence probability across Chicago using open crime data (2019–2025):
exploratory analysis, hotspot detection, a Random Forest classifier, and an interactive
Streamlit app that estimates crime probability for a given set of conditions.

**Author:** Rohith Sunkishala · UMBC M.S. Data Science Capstone (DATA 606), instructor Dr. Chaojie (Jay) Wang

## What this project does

- **Exploratory data analysis** — temporal, spatial, and categorical patterns in Chicago crime reports
  (`notebooks/01_exploratory_data_analysis.ipynb`)
- **Hotspot classification** — Random Forest model identifying likely crime hotspots from crime
  attributes, time features, and location context (`notebooks/02_crime_prediction_modeling.ipynb`)
- **Interactive predictor app** — enter a crime category, location type, hour, day, month, and year;
  get an estimated crime-occurrence probability with a low / medium / high risk band (`app/`)
- **Full write-up** — proposal, final report, and slide presentation (`docs/`)

## How the predictor is trained

The app's model is trained by `app/train_model.py`:

1. Each reported crime in `data/chicago_crimes_2019_2025.csv` becomes a **positive** example.
2. **Negative** examples are synthesized by sampling random feature combinations from the observed
   value distributions (none matching a real record) — a standard trick when only positive
   events are recorded.
3. A scikit-learn pipeline (`OneHotEncoder` + `RandomForestClassifier`) learns
   P(crime | crime category, location type, hour, day of week, month, year).

Because negatives are synthetic, the score is best read as a **relative risk indicator for demo
purposes**, not a safety forecast.

## Repository layout

```
├── app/
│   ├── app.py              # Streamlit crime-probability app
│   ├── train_model.py      # trains & saves the model the app loads
│   └── README.md
├── data/
│   ├── chicago_crimes_2019_2025.csv   # 1,000-row sample of Chicago open crime data
│   └── README.md
├── docs/
│   ├── proposal.md         # capstone proposal
│   ├── Report.md           # final report
│   └── Chicago_Crime_Presentation(1) (1) (1).pdf
└── notebooks/
    ├── 01_exploratory_data_analysis.ipynb
    └── 02_crime_prediction_modeling.ipynb
```

## Run it

```bash
pip install -r requirements.txt

# train the model the app loads (takes a few seconds)
python app/train_model.py

# launch the interactive app
streamlit run app/app.py
```

## Tech stack

Python · pandas · scikit-learn · Streamlit · joblib · matplotlib / seaborn

## Data source

City of Chicago open data portal — reported crimes 2019 to present
(`data.cityofchicago.org`). The CSV committed here is a 1,000-row sample used for the demo;
the notebooks document the full-data workflow.
