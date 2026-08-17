from datetime import  date
import smtplib
from email.message import EmailMessage
import random
import csv
import os

today_date = date.today()

letter_files = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
random_letter = random.choice(letter_files)

dict_data = {}

with open("birthdays.csv", "r") as f:
    birthdays = csv.DictReader(f)

    for row in birthdays:
        day = row["day"]
        month = row["month"]
        year = row["year"]
        name = row["name"]
        email = row["email"]
        DOB = f"{year}-{month}-{day}"
        dict_data.update({name: DOB})

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
recipient = email

for key, value in dict_data.items():
    if value == str(today_date):
        # print(key)
        with open(f"letter_templates/{random_letter}", "r") as f:
            letter = f.read()
            letter = letter.replace("[NAME]", key)
        print(letter)

        #configuring emails
        msg = EmailMessage()
        msg["Subject"] = f"{key}, It's your birthday!❤️"
        msg["From"] = MY_EMAIL
        msg["To"] = recipient
        msg.set_content(letter)

        # sending emails
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)

        print("Email sent successfully!")
