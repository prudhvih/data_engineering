# 📧 DataFrame Email Reporter (PostgreSQL → HTML → Email)

## 📌 Overview

This script fetches data from a PostgreSQL database, transforms it into a pivot table using pandas, 
converts it into an HTML table, and sends it via email using SMTP.


## 🚀 Features

* Execute SQL queries on PostgreSQL
* Transform data using pandas pivot tables
* Convert DataFrame to HTML format
* Send formatted email reports via Gmail SMTP



## 📥 Input Requirements

# 1. Database Connection

Provide a valid PostgreSQL connection string:

```python
postgresql://<user>:<password>@<host>:<port>/<database>
```

# 2. SQL Query

Modify the query as needed:

sql:: SELECT * FROM orders LIMIT 1000



# ⚙️ Email Configuration

Update sender and receiver details:

```python
msg['From'] = "your_email@gmail.com"
msg['To'] = "receiver_email@gmail.com"
```

### Gmail SMTP सेटअप:

* SMTP Server: `smtp.gmail.com`
* Port: `587`
* Use **App Password** (not your Gmail password)


## ▶️ How to Run

bash:
python script.py


## 🧠 How It Works

1. Fetch data from PostgreSQL using `pandas.read_sql()`
2. Create pivot table:

   * Index: `order_date`
   * Columns: `order_status`
   * Values: count of `order_id`

3. Convert pivot table to HTML
4. Embed HTML into email body
5. Send email using SMTP


## 📦 Libraries Used

| Library      | Purpose                         |
| ------------ | ------------------------------- |
| `pandas`     | Data processing & pivot table   |
| `smtplib`    | Sending emails                  |
| `email.mime` | Email formatting (HTML support) |


## ⚠️ Notes

* Ensure PostgreSQL is running and accessible
* Enable **App Passwords** in Gmail
* Avoid hardcoding credentials (use environment variables for security)


## 📌 Example Output

* Email containing an HTML table showing order counts grouped by date and status


## 🔐 Best Practice

Use environment variables instead of hardcoding credentials:

```bash
DB_URL=...
EMAIL_USER=...
EMAIL_PASS=...
```

## 👨‍💻 Use Case

Automated reporting system to send database summaries via email for monitoring or analytics.

