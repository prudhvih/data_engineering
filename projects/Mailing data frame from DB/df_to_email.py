import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def load_dfhtml(query,conn_url):
    df= pd.read_sql(query,conn_url)
    #datafram.pivot_table is a pandas API to convert dataframe to a pivot dataframe
    pivot = df.pivot_table(index='order_date',columns='order_status',values='order_id', aggfunc='count')
    html_table = pivot.to_html(index=True) 
    print("html table created successfully")
    return html_table

def process_mail():
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Your DataFrame Report"
    msg['From'] = "prudhvi203m@gmail.com"
    msg['To'] = "prudhvi.raj1597@gmail.com"
    #database connection details
    conn_url = 'postgresql://retail_db_userx:qwertyui123@localhost:5432/trn_retail_db'

    # SQL query to fetch from Database 
    query = '''
            SELECT * FROM orders LIMIT 1000'''

    # Embed the table into a basic HTML body
    html_body = f"""
    <html>
    <body>
        <p>Hi Shiva find the data below:</p>
        {load_dfhtml(query,conn_url)}
    </body>
    </html>
    """

    # Attach the HTML content
    msg.attach(MIMEText(html_body, 'html'))


    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        try:
            #your from email id and its app password 
            server.login("prudhvi203m@gmail.com", "one time generated 16 digit app password")
        except NameError as ne:
            print(ne)
        server.send_message(msg)
        print(f"mail sent to {msg['To']} successfully")


if __name__ == '__main__':
        print("hi")
        process_mail()
