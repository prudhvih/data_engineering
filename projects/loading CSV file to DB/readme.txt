CSV to PostgreSQL Data Loader(ETL Pipeline)

# Overview

This project provides a scalable Python-based solution to load CSV data into a PostgreSQL database.
It supports:

* Schema-driven column mapping
* Chunk-based processing for large files
* Parallel dataset loading using multiprocessing


# Features

* Load multiple datasets from a directory structure
* Automatic schema handling via JSON
* Efficient large file processing using chunks
* Parallel execution (up to 4 processes)
* Environment-based configuration using `.env`


# Project Structure

project/
│
├── main.py
├── schemas.json
├── .env
└── data/
    ├── dataset1/
    │   ├── part-00000
    │   ├── part-00001
    ├── dataset2/
```

# Input Requirements

1. Source Directory (`SRC_DIR`)

* Contains dataset folders
* Each dataset folder contains CSV files (e.g., `part-*`)

2. Schema File (`schemas.json`)

Defines structure for each dataset.

# Example:

```json
{
  "orders": [
    {"column_name": "order_id", "column_position": 1},
    {"column_name": "order_date", "column_position": 2},
    {"column_name": "order_customer_id", "column_position": 3}
  ]
}


#  Database Configuration

Create a `.env` file in the root directory:

SRC_DIR=path_to_data_directory
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
USER_PASSWORD=your_password
DB_NAME=your_database


# Connection URL Format:


postgresql://<user>:<password>@<host>:<port>/<database>


#  How to Run

1. Run for all datasets:

bash:- python main.py

2. Run specific datasets:

bash:- python main.py '["orders","customers"]'


# How It Works

1. Schema Loading

* Reads `schemas.json`
* Extracts column names in correct order

2. File Discovery

* Uses `glob` to find files:

<dataset>/part-*


3. Chunk Processing

* Reads CSV in chunks:

python:
pd.read_csv(..., chunksize=10000)

4. Database Load

* Uses pandas `to_sql()` to insert into PostgreSQL

5. Parallel Execution

* Uses `multiprocessing.Pool`
* Max 4 parallel dataset loads


 Libraries Used

| Library                   | Purpose                          |
| ------------------------- | -------------------------------- |
| `pandas`                  | CSV reading and database writing |
| `sqlalchemy` (via pandas) | Database connection              |
| `json`                    | Schema parsing                   |
| `glob`                    | File discovery                   |
| `re`                      | Path parsing                     |
| `dotenv`                  | Environment variable management  |
| `multiprocessing`         | Parallel processing              |
| `os`                      | OS-level operations              |
| `sys`                     | Command-line argument handling   |


# Database Schema Handling

* Table name = dataset name (`df_name`)
* Columns mapped using `schemas.json`
* Data appended (`if_exists='append'`)

For Customization

* Change chunk size:

python:
chunksize=10000

* Modify parallelism:

python:
pprocess_size = 4

Note:

* Ensure PostgreSQL tables exist before loading/duplicates may load
* Validate schema JSON before execution
* Use indexing on target tables for performance
* Avoid very large chunk sizes (memory risk)


# Example Use Case

Load retail datasets (`orders`, `customers`) into PostgreSQL for analytics pipelines or ETL workflows.

---


* Designed for scalable ETL pipelines
* Works best with structured batch data
* Can be extended to support other databases

#Flow Diagram (Data Pipeline)


        +----------------------+
        |   .env Configuration |
        | (DB + SRC_DIR setup) |
        +----------+-----------+
                   |
                   v
        +----------------------+
        |   process_files()    |
        +----------+-----------+
                   |
                   v
        +----------------------+
        | multiprocessing Pool |
        |  (parallel datasets) |
        +----------+-----------+
                   |
        +----------+-----------+
        |                      |
        v                      v
+---------------+      +---------------+
| process_dataset |    | process_dataset |
+-------+-------+      +-------+-------+
        |                      |
        v                      v
   +-------------------------------+
   |        db_loader()            |
   +---------------+---------------+
                   |
                   v
     +----------------------------+
     | Read schemas.json          |
     +----------------------------+
                   |
                   v
     +----------------------------+
     | Locate CSV files (part-*)  |
     +----------------------------+
                   |
                   v
     +----------------------------+
     | read_csv() (chunked read)  |
     +----------------------------+
                   |
                   v
     +----------------------------+
     | pandas DataFrame chunks    |
     +----------------------------+
                   |
                   v
     +----------------------------+
     | to_sql() → PostgreSQL      |
     +----------------------------+




ER Diagram (Logical View)


+-------------------+
|   schemas.json    |
+-------------------+
| dataset_name      |
| column_name       |
| column_position   |
+---------+---------+
          |
          | defines schema
          v
+-------------------+        loads into        +----------------------+
|   CSV Files       | -----------------------> |   PostgreSQL Tables  |
| (part-0000*)      |                         | (table = dataset)    |
+-------------------+                         +----------------------+
                                              | column_name          |
                                              | data (rows)          |
                                              +----------------------+


Data Flow Summary

1. `.env` provides configuration
2. `schemas.json` defines structure
3. CSV files are discovered using `glob`
4. Data is read in chunks using pandas
5. DataFrames are written to PostgreSQL tables
6. Multiple datasets are processed in parallel
