# Analyzing and Predicting Crime Hotspots and Patterns in Chicago 

**Prepared for:** UMBC Data Science Master’s Capstone  
**Instructor:** Dr. Chaojie (Jay) Wang  
**Author:** Sunkishala Rohith  

- **GitHub Repository:** [UMBC-DATA606-Capstone](https://github.com/sunkishalarohith853/UMBC-DATA606-Capstone)  
- **LinkedIn Profile:** [Rohith Sunkishala](https://www.linkedin.com/in/rohith-sunkishala-b08955333/)  
- **PowerPoint Presentation:** *to be added later*  
- **YouTube Demo Video:** *to be added later*  

---

## 1. Background  

Urban crime prevention remains a pressing issue worldwide, and cities like Chicago face ongoing challenges in ensuring public safety. Crime prediction provides valuable insights that help law enforcement agencies, policymakers, and communities allocate resources and adopt preventive strategies.  

The City of Chicago publishes a comprehensive open dataset of reported crimes. By focusing on data from **2019 to the present**, this project leverages recent patterns to build machine learning models for identifying hotspots and forecasting crime trends.  

### Project Objective  
This project aims to:  
- Detect potential crime hotspots across Chicago neighborhoods.  
- Forecast crime trends over time (daily, monthly, seasonal).  

### Why it Matters  
Accurate crime predictions support:  
- **Law enforcement:** More efficient patrol and resource allocation.  
- **City officials:** Insights into long-term safety trends.  
- **Communities:** Better awareness of risks and advocacy for prevention.  
- **Data science research:** Opportunities to evaluate fairness and ethics in predictive policing.  

### Research Questions  
1. Can we predict whether a given location and time will be a crime hotspot?  
2. Which features (e.g., day of week, month, community area, crime type) best explain crime occurrence?  
3. What seasonal or long-term crime patterns exist?  
4. How accurately can future crime counts be forecasted?  
5. What ethical and fairness concerns arise from predictive policing models?  

---

## 2. Data  

**Data Source**  
- **Dataset:** Crimes in Chicago (2019–Present)  
- **Provider:** [City of Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2)  
- **Size:** ~2.8 million rows × 22 columns (raw)  
- **Time Period:** 2019–Present  
- **Unit of Analysis:** Each row = one reported crime  

**Data Preparation**  
- **Selected Variables:** crime type, location, arrest flag, community area, date/time  
- **Engineered Features:**  
  - Temporal → hour, day of week, month, season  
  - Spatial → hotspot definitions (community area, grid-based)  
- **Target Variables:**  
  - Hotspot classification (binary: hotspot vs. non-hotspot)  
  - Crime count forecasting (numeric: crimes per time unit)  
- **Cleaning:** Removed identifiers and redundant fields  
- **Aggregation:** Data aggregated at **daily/weekly** intervals for trend analysis  

**Final Dataset**  
- After preprocessing: ~2.8 million rows × 13 columns  

| Column               | Type        | Definition                                | Example     |  
|-----------------------|------------|--------------------------------------------|-------------|  
| date                  | DateTime   | Crime occurrence date/time                 | 2022-07-10 23:45 |  
| primary_type          | Categorical| Type of crime                              | Theft       |  
| location_description  | Categorical| Where crime occurred                       | Street      |  
| arrest                | Binary     | 0 = No, 1 = Yes                            | 1           |  
| community_area        | Integer    | Chicago community area code                | 32          |  
| latitude              | Float      | Latitude                                   | 41.881      |  
| longitude             | Float      | Longitude                                  | -87.623     |  
| hour                  | Integer    | Hour of the day                            | 23          |  
| day_of_week           | Categorical| Day of the week                            | Friday      |  
| month                 | Integer    | Month (1–12)                               | 7           |  
| season                | Categorical| Season (Winter, Spring, Summer, Fall)      | Summer      |  
| hotspot               | Binary     | Target: 0 = Non-hotspot, 1 = Hotspot       | 1           |  
| crime_count           | Integer    | Crimes per time unit                       | 12          |  

---

## 3. Target Variables  

1. **Hotspot Classification (Binary)**  
   - 0 = Non-hotspot  
   - 1 = Hotspot  

2. **Trend Forecasting (Regression)**  
   - Predict numeric crime counts per time unit  

---

## 4. Feature Candidates  

- **Temporal:** hour, weekday/weekend, month, season  
- **Spatial:** community area, location description, latitude, longitude  
- **Crime-related:** crime type, arrest flag  
- **Aggregated:** moving averages, lag features, historical crime counts  

---

## 5. Two-Step Design  

This project adopts a **hybrid two-step design**:  

- **Step 1: Classification Model** → Predict whether a given time and location is a crime hotspot.  
- **Step 2: Time-Series Forecasting** → Forecast the number of crimes in future periods.  

### Benefits  
✅ Short-term predictions → operational planning  
✅ Long-term forecasts → policy-making & prevention strategies  

