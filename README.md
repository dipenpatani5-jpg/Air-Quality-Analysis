# Air Quality Analysis and Interactive Dashboard

**A Python-Based Data Analytics Project Using OpenAQ, Pandas, NumPy, Matplotlib, Seaborn, Plotly and Streamlit**

**Project Motto:** "Quality is our Motto."

---

## 1. Project Overview

Air pollution is one of the major environmental challenges affecting human health and the environment. Monitoring air quality and understanding pollution patterns are important for identifying pollution hotspots and studying changes in pollutant concentrations over time.

The **Air Quality Analysis and Interactive Dashboard** project focuses on collecting, processing, analyzing and visualizing air quality data from different monitoring stations using Python.

This project uses air quality data from the OpenAQ platform, which provides access to environmental measurements collected from monitoring stations around the world.

The collected data is processed using Pandas and NumPy, analyzed to identify pollution patterns, and visualized through Matplotlib and Seaborn.

An interactive web dashboard is developed using Streamlit and Plotly, allowing users to explore pollution measurements through filters, charts, statistical summaries and downloadable datasets.

### Project Objectives

- Collect air quality measurements from OpenAQ.
- Understand the structure of environmental datasets.
- Perform data cleaning and preprocessing.
- Analyze pollutant concentrations across different monitoring locations.
- Identify monthly pollution trends.
- Study correlations between pollutants and available weather measurements.
- Create meaningful data visualizations.
- Develop an interactive dashboard for exploring air quality data.
- Present analytical findings through a structured data analytics project.

---

## 2. Project Objectives and Scope

The primary objectives of this project are divided into the following areas.

### 2.1 Data Collection

- Access air quality data through the OpenAQ API.
- Retrieve monitoring station information.
- Collect sensor information from different locations.
- Download historical pollutant measurements.
- Store the collected information in CSV format.

### 2.2 Data Cleaning

- Identify missing values.
- Remove duplicate records.
- Convert date columns into appropriate datetime formats.
- Convert measurement values into numeric data types.
- Remove invalid records required for analysis.
- Generate a cleaned dataset.

### 2.3 Exploratory Data Analysis

- Understand dataset structure and dimensions.
- Calculate descriptive statistics.
- Identify available pollutants.
- Compare average pollution concentrations.
- Analyze pollution distribution across locations.
- Examine monthly changes in pollutant measurements.

### 2.4 Data Visualization

- Create monthly pollution trend charts.
- Compare pollution concentrations across monitoring stations.
- Generate correlation heatmaps.
- Identify positive and negative relationships between variables.

### 2.5 Interactive Dashboard

- Display important dataset statistics.
- Provide pollutant selection filters.
- Allow users to select monitoring locations.
- Filter data by date range.
- Display interactive charts.
- Allow users to download filtered datasets.

---

## 3. Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations and calculations |
| Requests | Connecting to the OpenAQ API |
| Matplotlib | Creating static visualizations |
| Seaborn | Statistical visualizations and heatmaps |
| Streamlit | Developing the interactive dashboard |
| Plotly | Creating interactive charts |
| OpenAQ API v3 | Collecting air quality measurements |
| Visual Studio Code | Development environment |

### Explanation of Libraries

**Python**

Python is used as the primary programming language because of its extensive ecosystem of data analytics libraries.

**Pandas**

Pandas is used for:
- Reading CSV files.
- Handling missing values.
- Removing duplicates.
- Grouping and aggregating records.
- Working with dates.
- Calculating average pollutant concentrations.

**NumPy**

NumPy supports numerical operations and array-based calculations used in data analysis.

**Matplotlib**

Matplotlib is used to create line charts and other static visualizations for understanding pollution trends.

**Seaborn**

Seaborn is used to create statistical visualizations, including bar charts and correlation heatmaps.

**Streamlit**

Streamlit converts Python analysis into an interactive web application without requiring separate frontend development.

**Plotly**

Plotly provides interactive charts with features such as zooming, hovering and exploring chart values.

**OpenAQ API**

OpenAQ is the external data source used to retrieve monitoring station information, sensor details and environmental measurements.

---

## 4. Project Folder Structure

The project is organized into separate Python scripts so that each component has a specific responsibility.

```text
Air_quality_index/
│
├── Data_set/
│
├── AirQuality.csv
├── AirQuality_Measurements.csv
├── Cleaned_AirQuality.csv
│
├── download_air_quality.py
├── download_measurements.py
│
├── data_cleaning.py
├── data_analyzing.py
│
├── data_visualization.py
├── seaborn_visualization.py
├── correlation_heatmap.py
│
├── app.py
│
├── PM25_Monthly_Trend.png
├── PM25_Location_Comparison.png
├── AirQuality_Correlation_Heatmap.png
│
├── requirements.txt
└── README.md
```

### Explanation of Project Files

| File | Responsibility |
|---|---|
| `download_air_quality.py` | Retrieves monitoring station information from OpenAQ. |
| `download_measurements.py` | Retrieves sensor measurements for available monitoring stations. |
| `AirQuality.csv` | Stores monitoring station information. |
| `AirQuality_Measurements.csv` | Stores the collected sensor measurements. |
| `data_cleaning.py` | Cleans and preprocesses the collected data. |
| `Cleaned_AirQuality.csv` | Stores the processed dataset. |
| `data_analyzing.py` | Performs exploratory data analysis and statistical calculations. |
| `data_visualization.py` | Creates the monthly PM2.5 trend graph. |
| `seaborn_visualization.py` | Creates the location-wise PM2.5 comparison chart. |
| `correlation_heatmap.py` | Generates the pollutant correlation heatmap. |
| `app.py` | Runs the interactive Streamlit dashboard. |
| `requirements.txt` | Lists the Python dependencies. |
| `README.md` | Provides complete project documentation. |

---

## 5. Dataset Description

### Data Source: OpenAQ

Website: https://openaq.org/

OpenAQ is an environmental data platform that provides access to air quality measurements from monitoring stations across different geographical locations.

This project uses OpenAQ API version 3 to retrieve air quality information.

### Dataset Components

**A. AirQuality.csv**

This file contains monitoring station information retrieved from the OpenAQ locations endpoint.

It includes available fields such as:

- Location ID
- Monitoring station name
- Geographic coordinates
- Country information
- Other available location metadata

**B. AirQuality_Measurements.csv**

This file contains the actual environmental measurements retrieved from monitoring sensors.

The dataset includes fields such as:

| Column | Description |
|---|---|
| Location_ID | Unique monitoring location identifier |
| Location | Name of the monitoring station |
| Sensor_ID | Unique sensor identifier |
| Pollutant | Name of the measured parameter |
| Value | Recorded measurement value |
| Date | Measurement timestamp |

The available measurements include air pollutants and meteorological parameters, depending on sensor availability.

Examples include:

- PM2.5 – Fine particulate matter.
- PM10 – Particulate matter.
- NO – Nitric Oxide.
- NO2 – Nitrogen Dioxide.
- NOx – Nitrogen Oxides.
- CO – Carbon Monoxide.
- O3 – Ozone.
- SO2 – Sulfur Dioxide.
- Temperature.
- Relative Humidity.
- Wind Speed.
- Wind Direction.

Not every monitoring station provides every parameter. Availability depends on the sensors installed at each station.

**C. Cleaned_AirQuality.csv**

This file contains the preprocessed dataset after cleaning operations.

It is used as the primary input for statistical analysis and visualizations.

---

## 6. Project Workflow

The complete project follows this data analytics pipeline:

```text
OpenAQ API
    |
    v
Monitoring Station Data
    |
    v
Sensor Data Collection
    |
    v
Raw Measurement Dataset
    |
    v
Data Cleaning
    |
    v
Cleaned Dataset
    |
    v
Exploratory Data Analysis
    |
    v
Data Visualization
    |
    v
Interactive Streamlit Dashboard
    |
    v
Final Insights and Reporting
```

Each stage has a separate responsibility, making the project easier to understand, maintain and extend.

---

## 7. Detailed Explanation of Python Components

### 7.1 download_air_quality.py

**Purpose:** Download monitoring station information from OpenAQ.

This script connects to the OpenAQ API and retrieves information about available monitoring locations.

Main operations:

1. Import the Requests and Pandas libraries.
2. Configure the OpenAQ API key.
3. Define the API endpoint.
4. Set request headers and parameters.
5. Send an HTTP GET request.
6. Receive the JSON response.
7. Convert the response into a Pandas DataFrame.
8. Export the results into `AirQuality.csv`.

**Important Python concepts used:**

- API integration.
- HTTP GET requests.
- JSON handling.
- Pandas DataFrames.
- CSV file operations.

### 7.2 download_measurements.py

**Purpose:** Collect actual pollution measurements from monitoring sensors.

This script retrieves measurements associated with the monitoring locations.

Main operations:

1. Load monitoring station information.
2. Extract location IDs.
3. Retrieve sensors associated with each location.
4. Identify sensor parameters.
5. Request historical measurement data.
6. Extract measurement values and timestamps.
7. Organize the results into a structured dataset.
8. Save the measurements in `AirQuality_Measurements.csv`.

**Important Python concepts used:**

- API endpoints.
- Nested JSON processing.
- For loops.
- Conditional statements.
- Lists and dictionaries.
- Pandas DataFrames.
- CSV export.

### 7.3 data_cleaning.py

**Purpose:** Prepare raw environmental measurements for analysis.

Data collected from external sources may contain missing values, duplicate records and inconsistent data types.

This script performs several preprocessing operations.

**Operations performed:**

1. Load the raw measurement dataset.
2. Display dataset information using `df.info()`.
3. Inspect the first five records using `df.head()`.
4. Identify missing values using `df.isnull().sum()`.
5. Identify duplicate records using `df.duplicated()`.
6. Remove duplicate records using `df.drop_duplicates()`.
7. Remove records with missing essential values.
8. Convert the Date column into datetime format.
9. Remove invalid date records.
10. Export the cleaned dataset.

**Cleaning methods used:**

```python
df.isnull().sum()

df.duplicated().sum()

df.drop_duplicates()

df.dropna(
    subset=["Value", "Date", "Pollutant"]
)

pd.to_datetime(
    df["Date"],
    errors="coerce"
)
```

The resulting dataset is saved as:

`Cleaned_AirQuality.csv`

**Project result:** The cleaning stage reduced the original 47,740 measurement records to 47,733 records. Seven records were removed during preprocessing.

### 7.4 data_analyzing.py

**Purpose:** Perform Exploratory Data Analysis (EDA).

EDA helps understand the dataset before creating visualizations.

The script performs the following operations.

**A. Descriptive Statistics**

```python
df.describe()
```

Calculates:
- Count.
- Mean.
- Standard deviation.
- Minimum.
- Maximum.
- Quartiles.

**B. Pollutant Analysis**

```python
df["Pollutant"].value_counts()
```

Identifies the number of measurements available for each pollutant.

**C. Average Pollution Analysis**

```python
df.groupby("Pollutant")["Value"].mean()
```

Calculates average measurements for each pollutant.

**D. Location Analysis**

```python
df.groupby("Location")["Value"].mean()
```

Calculates average measurements by monitoring location.

**E. Monthly Analysis**

The Date column is used to extract monthly information and calculate average measurements.

```python
df["Month"] = df["Date"].dt.month

df.groupby("Month")["Value"].mean()
```

These operations help identify the distribution of measurements across different months.

Different pollutants have different units. Their average concentrations should not be directly compared as though they were the same measurement.

### 7.5 data_visualization.py

**Purpose:** Visualize monthly PM2.5 pollution trends using Matplotlib.

This script focuses on PM2.5 measurements.

Main operations:

1. Load the cleaned dataset.
2. Convert dates into datetime format.
3. Filter PM2.5 records.
4. Extract monthly periods.
5. Calculate average monthly PM2.5 concentrations.
6. Create a line chart.
7. Add chart title and axis labels.
8. Add markers and grid lines.
9. Save the chart as a high-resolution PNG image.

**Visualization technique:** Line Chart.

**Generated file:** `PM25_Monthly_Trend.png`

The chart helps identify:

- Monthly pollution fluctuations.
- Periods with relatively high concentrations.
- Periods with relatively low concentrations.
- Changes in pollution levels over time.

### 7.6 seaborn_visualization.py

**Purpose:** Compare PM2.5 concentrations across monitoring locations.

The script groups PM2.5 measurements by location and calculates the average concentration.

Main operations:

1. Load the cleaned dataset.
2. Filter PM2.5 measurements.
3. Group data by monitoring location.
4. Calculate average PM2.5 concentration.
5. Sort locations in descending order.
6. Select the highest-ranking locations.
7. Generate a horizontal bar chart using Seaborn.
8. Save the chart.

**Visualization technique:** Horizontal Bar Chart.

**Generated file:** `PM25_Location_Comparison.png`

The chart helps identify:

- Locations with higher average PM2.5 measurements.
- Locations with lower average PM2.5 measurements.
- Differences between monitoring stations.

### 7.7 correlation_heatmap.py

**Purpose:** Understand relationships between pollutants and available environmental parameters.

This script creates a correlation matrix using Pandas and visualizes it through Seaborn.

Main operations:

1. Load the cleaned dataset.
2. Convert measurement values into numeric format.
3. Create a pivot table using date, pollutant and measurement values.
4. Calculate the correlation matrix.
5. Generate an annotated heatmap.
6. Apply a diverging colour palette.
7. Save the visualization.

**Visualization technique:** Correlation Heatmap.

**Generated file:** `AirQuality_Correlation_Heatmap.png`

The heatmap helps identify:

- Positive correlations.
- Negative correlations.
- Strong relationships.
- Weak relationships.

**Understanding correlation:**

- +1 indicates a perfect positive linear correlation.
- 0 indicates no linear correlation.
- -1 indicates a perfect negative linear correlation.

Correlation does not establish causation.

For scientifically stronger comparisons, measurements should be matched by both monitoring location and time.

### 7.8 app.py – Interactive Dashboard

**Purpose:** Develop a web-based dashboard for exploring air quality measurements.

The dashboard is developed using Streamlit and Plotly.

It allows users to explore the dataset without manually executing separate analysis scripts.

**Dashboard Components:**

**A. Page Configuration**

```python
st.set_page_config(
    page_title="Air Quality Dashboard",
    page_icon="",
    layout="wide"
)
```

Configures the dashboard title and page layout.

**B. Data Loading**

The dashboard loads `Cleaned_AirQuality.csv` using Pandas.

It also converts date and measurement columns into appropriate formats.

The `@st.cache_data` decorator helps avoid repeatedly loading the same dataset during normal Streamlit reruns.

**C. Sidebar Filters**

Users can select:

- Pollutant.
- Monitoring locations.
- Date range.

These filters dynamically update the dashboard results.

**D. KPI Cards**

The dashboard displays four important metrics:

1. Total Readings – Number of filtered measurements.
2. Monitoring Locations – Number of selected locations with records.
3. Average Concentration – Average measurement for the selected pollutant.
4. Selected Pollutant – Currently selected parameter.

**E. Monthly Pollution Trend**

An interactive Plotly line chart displays monthly average pollutant concentrations.

It helps users examine changes over time.

**F. Location Comparison**

A horizontal bar chart displays the highest average pollutant measurements across selected monitoring stations.

**G. Pollutant Distribution**

A doughnut chart displays the distribution of measurement records across different pollutant parameters for the selected period and locations.

This represents record counts, not the relative pollution contribution of each pollutant.

**H. Correlation Heatmap**

The dashboard creates a pivot table using date and location, then calculates correlations between pollutant measurements.

This helps explore relationships between parameters when matching observations are available.

**I. Data Table**

The dashboard displays filtered air quality records in an interactive table.

**J. Download Feature**

Users can download the filtered dataset in CSV format using Streamlit's download button.

---

## 8. Data Visualizations and Analytical Findings

The project contains three major static visualizations.

### Graph 1: Monthly PM2.5 Pollution Trend

**File:** `PM25_Monthly_Trend.png`

This line chart displays monthly average PM2.5 measurements over the available data period.

**Observations from the generated chart:**

- Pollution measurements fluctuate across different months.
- A significant increase is visible around November and December 2025.
- Relatively lower averages appear around July and August 2026.
- Another increase is visible in November 2026.

These observations identify periods requiring further investigation.

The last month in the downloaded dataset is November 2026, and the collection ends on November 20, so it represents an incomplete month.

### Graph 2: Location-wise PM2.5 Comparison

**File:** `PM25_Location_Comparison.png`

This horizontal bar chart compares average PM2.5 measurements across monitoring stations.

**Observations from the generated chart:**

- R K Puram, Delhi - DPCC appears among the highest locations.
- Burari Crossing, New Delhi - IMD also shows a high average.
- RIICO Industrial Area III, Bhiwadi - RSPCB shows relatively high measurements.
- Central University, Hyderabad - TSPCB appears among the lower locations in the displayed comparison.

The chart helps identify monitoring locations that may require closer examination.

### Graph 3: Air Pollution Correlation Heatmap

**File:** `AirQuality_Correlation_Heatmap.png`

The correlation heatmap displays relationships between environmental variables.

**Observations from the generated heatmap:**

- PM10 and PM2.5 show a strong positive correlation of approximately 0.88.
- NO2 and NOx show a strong positive correlation of approximately 0.87.
- Temperature and PM2.5 show a negative correlation of approximately -0.55.
- Temperature and NO2 show a negative correlation of approximately -0.53.

These results indicate statistical relationships within the analyzed dataset.

They should not be interpreted as proof that one parameter directly causes a change in another.

---

## 9. Installation and Setup Guide

Follow these steps to run the project on your computer.

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate to the project folder:

```bash
cd Air_quality_index
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Configure OpenAQ API Access

Create an OpenAQ account and obtain an API key.

Keep the API key private. For API download scripts, configure it using an environment variable or a local configuration file that is excluded from Git.

For example, on PowerShell:

```powershell
$env:OPENAQ_API_KEY="YOUR_API_KEY"
```

### Step 5: Download the Dataset

Execute:

```bash
python download_air_quality.py
```

Then:

```bash
python download_measurements.py
```

These scripts collect location information and sensor measurements using the OpenAQ API.

### Step 6: Perform Data Cleaning

```bash
python data_cleaning.py
```

This creates:

`Cleaned_AirQuality.csv`

### Step 7: Perform Data Analysis

```bash
python data_analyzing.py
```

### Step 8: Generate Visualizations

```bash
python data_visualization.py
```

```bash
python seaborn_visualization.py
```

```bash
python correlation_heatmap.py
```

### Step 9: Launch the Interactive Dashboard

```bash
streamlit run app.py
```

The dashboard normally opens at:

`http://localhost:8501`

---

## 10. Requirements

Create a `requirements.txt` file with the following dependencies:

```text
pandas
numpy
requests
matplotlib
seaborn
streamlit
plotly
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 11. Key Project Outcomes

The project demonstrates the complete data analytics workflow.

| Project Component | Outcome |
|---|---|
| Data Collection | Retrieved OpenAQ monitoring and sensor measurements |
| Data Cleaning | Processed 47,740 records into 47,733 records |
| Exploratory Analysis | Examined pollutant, location and monthly statistics |
| Matplotlib | Created monthly PM2.5 trend visualization |
| Seaborn | Created location comparison visualization |
| Correlation Analysis | Examined relationships between environmental parameters |
| Streamlit | Developed an interactive dashboard |
| Plotly | Created interactive data visualizations |

### Skills Demonstrated

- Python programming.
- Data collection through REST APIs.
- Data preprocessing.
- Data cleaning.
- Exploratory Data Analysis.
- Statistical analysis.
- Data visualization.
- Correlation analysis.
- Dashboard development.
- Working with real-world environmental datasets.

---

## 12. Limitations and Considerations

1. Data availability depends on the monitoring stations and sensors supported by OpenAQ.
2. Not all monitoring locations provide the same pollutant parameters.
3. Missing or incomplete measurements can influence statistical results.
4. Measurements from different sensors may have different coverage periods.
5. Pollutant concentrations should not be directly compared across different measurement units.
6. The current dashboard displays pollutant concentrations, not officially calculated AQI values.
7. Correlation does not establish causation.
8. The dashboard's results are limited to the data included in the downloaded CSV files.
9. The latest month may contain incomplete measurements.

### Future Improvements

- Add official AQI calculation using the relevant CPCB methodology.
- Include additional Indian monitoring stations.
- Integrate weather datasets for more detailed environmental analysis.
- Add geographical maps showing pollution levels.
- Develop automated data collection and updates.
- Add time-series forecasting for future pollution trends.
- Deploy the dashboard online using Streamlit Community Cloud or another hosting platform.
- Add downloadable analytical reports.

---

## 13. Conclusion

The Air Quality Analysis project demonstrates how Python can be used to transform raw environmental measurements into meaningful analytical insights.

Starting with data collection through OpenAQ, the project follows a complete data processing workflow involving data cleaning, exploratory analysis, statistical calculations and visualization.

Pandas and NumPy are used for data processing and analysis, while Matplotlib and Seaborn help identify pollution patterns and relationships between environmental variables.

The Streamlit dashboard provides an interactive interface through which users can explore pollutant concentrations, compare monitoring stations, analyze trends and download filtered datasets.

Overall, this project helped develop practical experience in Python-based data analytics, API integration, data preprocessing, statistical analysis, visualization and interactive dashboard development.

The ultimate objective is to transform environmental data into understandable information that can support better awareness and further investigation of air pollution.

---

## 14. Author Information

**Name:** Dipen Patni

**Project Title:** Air Quality Analysis and Interactive Dashboard

**Technical Skills:** Python, Data Analytics, Data Visualization, Dashboard Development

**Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn, Streamlit, Plotly and OpenAQ API.

---

## 15. Acknowledgements

- [OpenAQ](https://openaq.org/) – Air quality data source.
- [Pandas](https://pandas.pydata.org/) – Data manipulation and analysis.
- [NumPy](https://numpy.org/) – Numerical computing.
- [Matplotlib](https://matplotlib.org/) – Data visualization.
- [Seaborn](https://seaborn.pydata.org/) – Statistical visualization.
- [Streamlit](https://streamlit.io/) – Interactive dashboard development.
- [Plotly](https://plotly.com/python/) – Interactive visualizations.

---

**Thank you for reviewing this project.**
