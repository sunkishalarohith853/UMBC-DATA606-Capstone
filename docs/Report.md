# Chicago Crime Probability Prediction
### **Rohith Sunkishala— Fall 2025**

**YouTube Presentation:** *[]*  
**Final PPT:** *[https://github.com/sunkishalarohith853/UMBC-DATA606-Capstone/blob/main/docs/Chicago_Crime_Presentation(1)%20(1)%20(1).pdf]*  
**GitHub Repository:** *[https://www.linkedin.com/in/rohith-sunkishala-b08955333/]*  

---

## 1. Background

Crime prediction plays a vital role in supporting community safety, resource allocation, and strategic decision-making. Chicago provides one of the most detailed publicly available crime datasets in the United States, making it ideal for building predictive crime models.

This project aims to **estimate the probability of a crime occurring at a given time and location** using machine learning techniques.  
The project includes:

- Exploratory Data Analysis (EDA)  
- Crime trend and density analysis  
- Feature engineering  
- Machine learning model development  
- A Streamlit web application for real-time prediction  

---

## 2. Data Sources

The dataset is sourced from the **Chicago Data Portal** and includes crime incidents from **2019–2025**.

### Key Data Fields:
- Crime type (Theft, Battery, etc.)
- Date and time of incident
- Location description
- Domestic vs. non-domestic flag
- Latitude and longitude
- Arrest status
- Case ID / incident ID

The dataset is robust, diverse, and continuously updated, making it suitable for building crime prediction models.

---

## 3. Data Elements

The final cleaned dataset contained the following main elements:

### **Categorical Features**
- Primary crime type  
- Location description  
- Domestic flag  
- District & community area  

### **Temporal Features (Engineered)**
- Year  
- Month  
- Weekday  
- Hour  

### **Spatial Features**
- Latitude  
- Longitude  

### **Target Variable**
The dataset originally contained **only crime events**, so synthetic "no-crime" samples were generated:

- `1` → Crime occurred  
- `0` → Synthetic non-crime sample  

This balancing was essential for probability-based classification.

---

## 4. Exploratory Data Analysis (EDA)

### **4.1 Crime Type Analysis**
- Theft, Battery, and Criminal Damage were the most frequent crimes.
- Theft contributed the highest share of incidents.
- Identifying major crime types helped shape model features.

### **4.2 Crime Trends (2019–2025)**
- Clear yearly variation in crime rates.
- **2024 showed the highest total number of crimes.**
- Seasonal patterns and long-term trends influenced modeling.

### **4.3 Domestic vs. Non-Domestic Crimes**
- ~81% of crimes were **non-domestic**.
- ~19% were **domestic**.
- This imbalance helped identify different behavioral patterns in crime.

### **4.4 Weekly Crime Patterns**
- **Fridays** had the highest crime counts.
- **Tuesdays and Thursdays** showed the lowest.
- Weekly cycles were incorporated into features to capture temporal patterns.

### **4.5 Crime Density Mapping**
- Heatmaps revealed high-crime hotspots concentrated in **North-East Chicago**.
- Spatial clustering supported hotspot-based feature design.
- Mapping confirmed the importance of latitude & longitude in prediction.

---

## 5. Feature Engineering

Key engineering steps include:

- Extracted **hour, weekday, month, year** from timestamps.
- One-Hot Encoded all major categorical features.
- Normalized numerical variables.
- Removed irrelevant or missing attributes.
- Balanced dataset using **synthetic negative sampling**.
- Prepared structured data for ML modeling.

---

## 6. Machine Learning Models

### **Model Used: Random Forest Classifier**
The Random Forest algorithm was chosen because:

- It handles mixed numeric + categorical data well.  
- Robust to outliers and noise.  
- Provides reliable probability outputs.  
- Performs effectively on large datasets.  

### **Training Process**
- Split into training and test sets.
- Tuned hyperparameters for optimal performance.
- Evaluated model using accuracy, probability metrics, and confusion matrix.

### **Synthetic Negative Sampling**
Since real data contains only crime events, the model would always predict “crime.”  
To avoid this bias:

- Generated synthetic (0) samples with random time + location combinations.
- Combined with real crime events to create a balanced dataset.
- Allowed the classifier to learn *where/when* crimes are unlikely.

---

## 7. Results

### **Model Performance**
- Strong predictive accuracy on test data.  
- Good separation between classes.  
- Reliable probability scores useful for real-time predictions.  

### **Key Insights**
- Time and location significantly influence crime probability.
- Certain crime types heavily cluster in specific neighborhoods.
- Predictive accuracy improved after adding engineered temporal features.

---

## 8. Streamlit Web Application

A Streamlit-based application was developed to make predictions user-friendly.

### **App Features**
- User inputs:  
  - Time (hour, weekday, month)  
  - Location (latitude, longitude)  
  - Crime type  

- Outputs:
  - Probability of a crime occurring  
  - Risk level: **Low / Medium / High**  
  - Clean, dark-themed UI  

This tool demonstrates real-time predictive capability and supports public-safety decisions.

---

## 9. Conclusion

This project successfully developed a machine learning–based system to estimate the likelihood of crime in Chicago. The model provides actionable insights that:

- Support law enforcement resource allocation  
- Enhance community safety strategies  
- Help identify high-risk times and locations  

The predictive app delivers a practical interface for real-time usage.

---

## 10. Limitations

- Synthetic negative sampling may not perfectly represent real no-crime conditions.  
- Dataset does not include socioeconomic or weather variables that may influence crime.  
- GPS coordinates sometimes contain missing or incorrect values.  
- Crime records rely on reported incidents only (underreporting exists).  

---

## 11. Future Research Directions

Future enhancements could include:

- Integrating **real-time streaming data** from Chicago Police.  
- Adding **weather, census, and socioeconomic datasets**.  
- Using advanced models such as **XGBoost, LSTMs, or Spatiotemporal Neural Networks**.  
- Deploying on AWS or GCP for public web access.  
- Improving negative sampling by modeling realistic no-crime distributions.  

---

**End of Report**  
