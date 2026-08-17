PYTHON

import os
from datetime import datetime
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Specify your Excel filename (must include .xlsx)
EXCEL_FILE = 'students.xlsx'

def get_excel_data():
    """Reads existing data from the Excel file to display on the webpage."""
    if not os.path.exists(EXCEL_FILE):
        return []

    # Read Excel file using openpyxl engine
    df = pd.read_excel(EXCEL_FILE, engine='openpyxl').fillna('')
    
    submissions = []
    for _, row in df.iterrows():
        submissions.append({
            'submitted_at': str(row.get('Date Submitted', '')),
            'student_name': str(row.get('Student Name', '')),
            'grade': str(row.get('Grade', '')),
            'favorite_subject': str(row.get('Favorite Subject', ''))
        })
    return submissions

@app.route('/', methods=['GET', 'POST'])
def home():
    message = None

    if request.method == 'POST':
        # 1. Capture inputs from HTML form
        student_name = request.form.get('student_name')
        grade = request.form.get('grade')
        favorite_subject = request.form.get('favorite_subject')
        submitted_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 2. Read existing Excel file or create new DataFrame structure
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
        else:
            df = pd.DataFrame(columns=['Date Submitted', 'Student Name', 'Grade', 'Favorite Subject'])

        # 3. Create new row
        new_row = pd.DataFrame([{
            'Date Submitted': submitted_at,
            'Student Name': student_name,
            'Grade': grade,
            'Favorite Subject': favorite_subject
        }])

        # 4. Append new row and save back to Excel
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

        message = f"Successfully added {student_name} to Excel!"

    # Load updated submissions to show in the HTML table
    submissions = get_excel_data()

    return render_template('index.html', message=message, submissions=submissions)

if __name__ == '__main__':
    app.run(debug=True)
