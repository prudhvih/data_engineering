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


Briefly..


# 📂 CSV to JSON File Converter

## 📌 Overview

This script converts CSV files into JSON format using a schema-driven approach.
It reads CSV files from a source directory, applies column structure from a schema file, and writes the output as JSON files.


## 🚀 Features

* Schema-based column mapping
* Batch processing of multiple datasets
* Converts CSV → JSON (line-delimited format)
* Environment-based configuration using `.env`
* Handles multiple files (`part-*`) per dataset



## 📥 Input Requirements

### 1. Source Directory (`SRC_FILE_PATH`)

* Contains dataset folders
* Each dataset folder includes CSV files:

```text
dataset_name/
  ├── part-00000
  ├── part-00001
```

### 2. Schema File (`schemas.json`)

Defines column names and order for each dataset.

### Example:

```json
{
  "orders": [
    {"column_name": "order_id", "column_position": 1},
    {"column_name": "order_date", "column_position": 2}
  ]
}
```



## 📤 Output

* JSON files stored in target directory (`TGT_FILE_PATH`)
* Structure:

```text
target/
  └── orders/
        ├── part-00000
        ├── part-00001
```

* Format: **JSON Lines (one record per line)**


## ⚙️ Configuration

Create a `.env` file:

```env
SRC_FILE_PATH=path_to_source_directory
TGT_FILE_PATH=path_to_target_directory
```



## ▶️ How to Run

### Run all datasets:

```bash
python script.py
```

### Run specific datasets:

```bash
python script.py '["orders","customers"]'
```

---

## 🧠 How It Works

1. Load environment variables (`.env`)
2. Read schema from `schemas.json`
3. Identify CSV files using `glob` (`part-*`)
4. Read CSV using pandas
5. Apply column names based on schema
6. Convert and write to JSON format

---

## 📦 Libraries Used

| Library  | Purpose                         |
| -------- | ------------------------------- |
| `pandas` | CSV reading and JSON writing    |
| `json`   | Schema handling                 |
| `glob`   | File discovery                  |
| `re`     | Path parsing                    |
| `dotenv` | Environment variable management |
| `os`     | File and directory handling     |
| `sys`    | Command-line arguments          |

---

## ⚠️ Notes

* Ensure schema matches CSV structure
* Output files overwrite if rerun
* Missing dataset folders are skipped with error message

---

## 📌 Use Case

Useful for data pipelines where CSV data needs to be transformed into JSON format for APIs, storage, or downstream processing.
