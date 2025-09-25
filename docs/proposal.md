# Predicting Crime Hotspots and Trends in Chicago

### Prepared for: UMBC Data Science Master’s Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  
**Author:** [Your Full Name]

- **GitHub Repository:** (to be added later)  
- **LinkedIn Profile:** (to be added later)  
- **PowerPoint Presentation:** (to be added later)  
- **YouTube Demo Video:** (to be added later)

---

## 1. Background

Crime prediction is a critical challenge for cities worldwide. Law enforcement agencies need data-driven insights to anticipate where and when crimes are likely to occur in order to allocate resources effectively and enhance public safety.

The city of Chicago provides an open dataset of reported crimes dating back to 2001, which offers an opportunity to apply data science methods to analyze spatial and temporal crime patterns.

### Project Objective

This project aims to build predictive models that:

1. Identify potential crime hotspots across Chicago neighborhoods.  
2. Forecast crime trends over time (daily, monthly, seasonal).

### Why it Matters

Accurate crime prediction helps:

- Law enforcement allocate patrols and resources more efficiently.  
- City officials identify long-term safety trends.  
- Communities understand risks and advocate for preventive measures.  
- Data scientists explore fairness and ethical considerations in predictive policing.

### Research Questions

- Can we predict whether a given location and time will be a crime hotspot?  
- Which features (day of week, season, community area, crime type) are most predictive of crime?  
- What seasonal or long-term trends can be identified in crime occurrences?  
- How accurately can crime counts be forecasted into the future?  
- What ethical and fairness issues arise when using predictive models in public safety?

---

## 2. Data

### Data Source

- **Dataset:** Crimes in Chicago, 2001–Present  
- **Provider:** City of Chicago Data Portal  
- **Size:** ~6 million records  
- **Time Period:** 2001–Present  
- **Unit of Analysis:** One row per reported crime

### Data Preparation

- **Selected Variables:** crime type, location, arrest flag, community area, date/time  
- **Engineered Features:**
  - **Temporal:** hour, day of week, month, season  
  - **Spatial:** hotspot definitions by community area or grid cells  
  - **Target Variables:**
    - **Hotspot Classification:** 1 = hotspot, 0 = non-hotspot  
    - **Crime Count Forecasting:** number of crimes per time unit  
- **Cleaning:** Removed identifiers or redundant fields  
- **Aggregation:** Data aggregated at community area and daily/weekly time intervals for trend analysis

### Final Dataset: Columns and Data Types

| Column              | Type        | Definition                                  | Example            |
|---------------------|-------------|---------------------------------------------|--------------------|
| `date`              | DateTime    | Date and time of crime occurrence           | 2017-03-10 23:45   |
| `primary_type`      | Categorical | Type of crime (e.g., theft, assault)        | Theft              |
| `location_description` | Categorical | Location where crime occurred          | Street             |
| `arrest`            | Binary      | 0 = No, 1 = Yes                              | 1                  |
| `community_area`    | Integer     | Chicago community area code                 | 32                 |
| `latitude`          | Float       | Latitude of crime occurrence                | 41.881             |
| `longitude`         | Float       | Longitude of crime occurrence               | -87.623            |
| `hour`              | Integer     | Hour of the day (derived from timestamp)    | 23                 |
| `day_of_week`       | Categorical | Day name derived from timestamp             | Friday             |
| `month`             | Integer     | Month (1–12)                                 | 3                  |
| `season`            | Categorical | Season of the year                          | Spring             |
| `hotspot`           | Binary      | Target 1: 0 = Non-hotspot, 1 = Hotspot      | 1                  |
| `crime_count`       | Integer     | Target 2: Crimes per time unit              | 12                 |

---

## 3. Target Variables

### 1. **Hotspot Classification (Binary)**
- `0` = Non-hotspot  
- `1` = Hotspot

### 2. **Trend Forecasting (Regression)**
- Numeric prediction of crime counts per time unit

---

## 4. Feature Candidates

- **Temporal Features:** hour, day, weekday/weekend, month, season  
- **Spatial Features:** community area, location description, latitude, longitude  
- **Crime Features:** type of crime, arrest flag  
- **Aggregated Features:** moving averages, lag variables, prior period crime counts

---

## 5. Two-Step Design

This project uses a two-step predictive design:

### Step 1: Classification Model
Predict whether a given time and location is a crime **hotspot** (Yes/No).

### Step 2: Time-Series Forecasting
Predict the **number of crimes** that will occur in future time periods.

This hybrid design provides:

- ✅ **Short-term predictions** for operational planning  
- ✅ **Long-term forecasts** for policy and prevention strategies

---

