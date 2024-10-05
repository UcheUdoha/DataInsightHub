import csv
from pymongo import MongoClient

class User:
    def __init__(self, data):
        self.age = data['age']
        self.gender = data['gender']
        self.total_income = data['total_income']
        self.expenses = data['expenses']
    
    @staticmethod
    def save_to_csv(users, filename='users_data.csv'):
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write the header
                writer.writerow(['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
                # Write user data
                for user in users:
                    writer.writerow([
                        user['age'], 
                        user['gender'], 
                        user['total_income'],
                        user['expenses']['utilities'],
                        user['expenses']['entertainment'],
                        user['expenses']['school_fees'],
                        user['expenses']['shopping'],
                        user['expenses']['healthcare']
                    ])
            print(f"Data successfully written to {filename}.")
        except Exception as e:
            print(f"An error occurred while writing to CSV: {e}")

# MongoDB client setup
try:
    client = MongoClient('mongodb://localhost:27017/')
    db = client.survey_db
    collection = db.user_data
    print("Connected to MongoDB successfully.")
except Exception as e:
    print(f"An error occurred while connecting to MongoDB: {e}")

# Fetch data from MongoDB
try:
    users_data = list(collection.find())
    if not users_data:
        print("No data found in the collection.")
    else:
        # Save data to CSV
        User.save_to_csv(users_data)
except Exception as e:
    print(f"An error occurred while fetching data from MongoDB: {e}")