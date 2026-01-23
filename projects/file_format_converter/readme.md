* CSV to JSON Converter 

This application converts CSV files into JSON format using a predefined schema.

The data folder contains:

db_csv/: Source directory that holds 6 CSV files, each inside its own folder.

db_json/: Target directory where all converted JSON files will be stored.

.env
Contains environment variables (such as source and target paths). These variables are loaded at runtime using load_dotenv().

requirements.txt
Lists all required Python libraries needed to run the application.

Setup Instructions
1. Create a virtual environment
python -m venv ffc-venv

2. Activate the virtual environment

(activate command depends on your OS)

3. Install required dependencies
pip install -r ./requirements.txt

4. Running the Application
Convert all CSV files
python app.py

This will convert all 6 CSV files from db_csv into JSON files and store them in db_json.

5. Convert selected CSV files only
python app.py '[\"orders\",\"products\"]'

This will convert only the specified CSV datasets.

6. Libraries Used

The following Python libraries are used in the application:

os – Reads environment variables and handles file paths

sys – Reads command-line arguments

glob – Lists CSV files from source directories

json – Reads the schema file that defines table structure

pandas – Reads CSV files and writes JSON output

re – Splits file paths to extract dataframe names