from flask import Flask, render_template, request, flash, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from user import User

# Load environment variables
load_dotenv(override=True)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "development-secret-key")

# Connect to MongoDB
host = os.getenv("MONGODB_HOST")
username = os.getenv("MONGODB_USERNAME")
password = os.getenv("MONGODB_PASSWORD")

client = MongoClient(
    f"mongodb+srv://{host}/",
    username=username,
    password=password,
    authSource="admin"
)

db = client["HealthcareSurvey"]
collection = db["survey_responses"]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Collect personal information
        age = int(request.form["age"])
        gender = request.form["gender"]
        total_income = float(request.form["total_income"])

        # Collect selected expense categories
        selected_categories = request.form.getlist("expense_categories")

        expenses = {}

        for category in selected_categories:

            amount = request.form.get(f"{category}_amount")

            if not amount:
                flash(f"Please enter an amount for {category}.")
                return render_template("index.html")

            expenses[category] = float(amount)
            
        # Prepare participant record
        participant = User(
            age=age,
            gender=gender,
            total_income=total_income,
            expenses=expenses
        )

        # Save participant record to MongoDB
        try:
            collection.insert_one(participant.to_dict())
            flash("Thank you! Your survey response was submitted successfully.")

        except Exception as e:
            print("Database save error:", repr(e))
            flash("Sorry, we could not save your response. Please try again.")

        # Save participant record to MongoDB
        try:
            collection.insert_one(participant.to_dict())
            flash("Thank you! Your survey response was submitted successfully.")

        except Exception as e:
            print("Database save error:", repr(e))
            flash("Sorry, we could not save your response. Please try again.")

        return redirect(url_for("home"))

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)), debug=False)