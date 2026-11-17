# Healthcare Survey Data Collection and Analysis

## 1. Project Overview

This project is a web-based healthcare survey application developed using Python and Flask. It collects demographic and financial information from respondents, stores the submissions in MongoDB Atlas, exports the collected records into CSV format, and analyses the data using Python in Jupyter Notebook.

The project demonstrates the use of web development, database management, data processing and data visualisation.

## 2. Technologies Used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- Pandas
- Matplotlib
- Jupyter Notebook
- Git and GitHub
- Render (web application deployment)

## 3. Survey Information Collected

The application collects:

- Age
- Gender
- Total income
- Utilities expenditure
- Entertainment expenditure
- School fees expenditure
- Shopping expenditure
- Healthcare expenditure

Respondents can select expense categories and enter the corresponding amounts.

## 4. Project Structure

```text
Health_Survey_Project/
│
├── app.py
├── user.py
├── export_data.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── survey_data.csv
├── survey_data_cleaned.csv
│
├── Health_Survey_Analysis.ipynb
├── age_income_relationship.png
└── gender_spending_comparison.png
```

## 5. Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/Wonderstar11/healthcare-survey-project.git
```

### Step 2: Navigate into the project folder

```bash
cd healthcare-survey-project
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure MongoDB

Create a MongoDB Atlas database and configure the following environment variables:

- `MONGODB_HOST`
- `MONGODB_USERNAME`
- `MONGODB_PASSWORD`

For local development, these can be stored in a `.env` file in the project directory.

**Important:** Never upload the `.env` file or database credentials to GitHub.

## 6. Running the Flask Application

After configuring MongoDB, start the application with:

```bash
python app.py
```

Open the local address displayed in the terminal to access the survey webpage.

## 7. Data Export and Processing

The `user.py` file contains a Python class named `User`, which represents the respondent's demographic and financial information.

The `export_data.py` script retrieves survey submissions from MongoDB and exports the collected records into:

`survey_data.csv`

The exported dataset is then cleaned by removing duplicate records. The cleaned data is saved as:

`survey_data_cleaned.csv`

## 8. Data Analysis and Visualisation

The Jupyter Notebook `Health_Survey_Analysis.ipynb` loads the survey data and performs descriptive analysis.

The analysis includes:

- Dataset inspection and duplicate removal.
- Descriptive statistics.
- Gender distribution.
- Average expenditure across spending categories.
- Relationship between age and total income.

### Exported Visualisations

**Age and Income Relationship**

`age_income_relationship.png`

**Average Spending by Gender Across Expense Categories**

`gender_spending_comparison.png`

Both charts are exported as PNG images for use in presentations.

## 9. Deployment

The Flask application is deployed using Render.

The live application is accessible at:

https://healthcare-survey-project.onrender.com/

MongoDB Atlas is used as the cloud database for storing survey submissions.

## 10. Limitations

The dataset used for the analysis contains five unique sample responses after duplicate removal.

Consequently, the findings are preliminary and should not be treated as representative of a larger population. A larger dataset would be required for more reliable conclusions.

The application is deployed on Render rather than AWS.

## 11. Conclusion

This project demonstrates the integration of Flask, MongoDB and Python for collecting, storing, processing and analysing healthcare survey data.

It also demonstrates how data visualisation can be used to communicate patterns in income and expenditure.