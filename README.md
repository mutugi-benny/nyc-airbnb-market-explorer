# NYC Airbnb Market Explorer

A data engineering project that ingests, cleans, and analyzes NYC Airbnb market data to provide actionable insights for real estate and hospitality businesses.

## 🎯 Project Overview

Real estate companies struggle to ingest data from multiple file formats and extract accurate market insights. This project builds a complete data pipeline that:
- Ingests Airbnb data from CSV
- Cleans strings and formats dates
- Combines datasets
- Produces market summary reports

## 📊 Key Insights

- Average price per night: **$167.66**
- Monthly Airbnb cost: **$1,945.09** 
- Total listings analyzed: **36,800+** 

## 🛠️ Tech Stack

- **Language**: Python 3.14+
- **Libraries**: pandas, numpy, matplotlib, seaborn
- **Environment**: Jupyter Notebook
- **Version Control**: Git + GitHub

## 📁 Project Structure
nyc-airbnb-market-explorer/
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned data
├── src/
│ ├── 01_data_import.ipynb
│ ├── 02_data_cleaning.ipynb
│ └── 03_data_analysis.ipynb
├── output/
│ ├── market_summary_report.md
│ └── visualizations/
└── README.md

## 🚀 Setup Instructions

```bash
# 1. Clone repository
git clone <your-github-repo-url>
cd nyc-airbnb-market-explorer

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Download dataset
# Visit: https://www.kaggle.com/datasets/dominoweir/inside-airbnb-nyc
# Save to data/raw/listings.csv

# 5. Run notebooks
jupyter notebook src/01_data_import.ipynb
jupyter notebook src/02_data_cleaning.ipynb
jupyter notebook src/03_data_analysis.ipynb
```

## 📈 Key Skills Demonstrated

|        Skill           |              Description                |
|--------- --------------|-----------------------------------------|
|     Data Importing     |      CSV, multiple file formats         |
|   Data Exploration     |    `head()`, `describe()`, `info()`     |
|    Data Cleaning       |    Strings, dates, missing values       |
| Feature Engineering    | Creating new columns from existing data |
|     Data Merging       |      Joining multiple DataFrames        |
|     Data Analysis      |     Group statistics, aggregations      |

## 📄 Deliverables

1. **Cleaned Dataset**: `data/processed/cleaned_airbnb_data.csv`
2. **Market Summary Report**: `output/market_summary_report.md`
3. **Visualizations**: 3 charts (PNG format)
4. **Top Neighborhoods**: `output/top_neighborhoods.csv`
5. **Full Code**: 3 Jupyter Notebooks with comments

## 📚 References

- Dataset: [Inside Airbnb NYC](http://insideairbnb.com/new-york-city/) 

## 📝 License

MIT License