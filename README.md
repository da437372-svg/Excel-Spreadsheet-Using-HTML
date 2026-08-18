# Flask to Excel Data Logger
A beginner-friendly Flask web application that takes user input from an HTML form and automatically logs the data row-by-row into a local Microsoft Excel spreadsheet (`.xlsx`). 

> 💡 **Note for Beginners:** I built this project using **AI code generation** to help create and refine the Python backend logic. This guide is written specifically to help other beginners understand how the files connect and how to run the app step-by-step!

# 📁 Project Structure

To run a Flask app, your files **must** be organized in a specific structure. Create a folder named `templates` in your project folder and place your HTML file inside it:
```text
flask-excel-app/
│
├── app.py              # Main Python code (Backend)
├── students.xlsx       # Excel file (Created automatically on first run)
└── templates/          # Required folder for Flask HTML templates
    └── index.html      # HTML form interface (Frontend)
```
# 🛠️ How It Works
<ins>**1. Frontend (templates/index.html)**</ins>
* The HTML file provides a form for users to enter information (such as student name, grade, and favorite subject). When submitted, it sends a POST request containing the input data back to the Flask server.

<ins>**2. Backend (app.py)**</ins>

The Python backend uses Flask to host the server and Pandas + OpenPyXL to interact with Excel:

* Captures the form inputs when the user clicks Submit.

* Reads the local Excel file (or creates students.xlsx if it doesn't exist yet).

* Appends the new submission as a new row with a timestamp.

* Reloads the table on the webpage to display all saved submissions.

  ## 💻 Python Code (app.py)

* The following app.py link will open a page of a generated code for the flask project, which should be pasted on the python code engine you will use
> [app.py](/app.py) 

# 🚀 Step-by-Step Instructions to Run

<ins>**1. Install Required Python Libraries**</ins>

* Open your terminal or command prompt and run:

   ```
  pip install flask pandas openpyxl
  ```
  
 <ins>**2. Run the App**</ins>

* Navigate to your project directory in the terminal and start the Flask server:

```
python app.py
```

<ins>**3. Open in Browser**</ins>

* Open your web browser and go to the provided link in your terminal after running the python app.py

  # ⚠️ Common Troubleshooting Tips

  * Permission Error: Make sure the ``students.xlsx`` file is closed in Microsoft Excel on your computer while running the app. Windows locks open files, which prevents Python from saving new rows.
  * Missing Engine Error: If you get a ``ValueError: No engine for filetype,`` ensure ``engine='openpyxl'`` is explicitly passed into ``read_excel()`` and ``to_excel()``calls.
