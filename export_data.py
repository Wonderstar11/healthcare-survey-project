import os
import csv
from pymongo import MongoClient
from dotenv import load_dotenv

# Load MongoDB credentials
load_dotenv(override=True)

host = os.getenv("MONGODB_HOST")
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

# Connect to MongoDB
client = MongoClient(
    f"mongodb+srv://{host}/",
    username=username,
    password=password,
    authSource="admin",
    serverSelectionTimeoutMS=15000
)

db = client["HealthcareSurvey"]
collection = db["survey_responses"]

# Retrieve survey responses, excluding test records
responses = collection.find({"record_type": {"$ne": "test"}})

# Define CSV columns
fieldnames = [
    "age",
    "gender",
    "total_income",
    "utilities",
    "entertainment",
    "school_fees",
    "shopping",
    "healthcare"
]

# Export responses to CSV
output_file = os.path.join(
    os.path.dirname(__file__),
    "survey_data.csv"
)

count = 0

try:
    client.admin.command("ping")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for response in responses:
            expenses = response.get("expenses", {})

            row = {
                "age": response.get("age", ""),
                "gender": response.get("gender", ""),
                "total_income": response.get("total_income", ""),
                "utilities": expenses.get("utilities", ""),
                "entertainment": expenses.get("entertainment", ""),
                "school_fees": expenses.get("school_fees", ""),
                "shopping": expenses.get("shopping", ""),
                "healthcare": expenses.get("healthcare", "")
            }

            writer.writerow(row)
            count += 1

    print("CSV export completed successfully!")
    print("Total survey responses exported:", count)
    print("File saved to:", output_file)

except Exception as e:
    print("Export failed:", repr(e))

finally:
    client.close()