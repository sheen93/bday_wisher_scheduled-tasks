# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

current_dt = dt.datetime.now()

df = pandas.read_csv("birthdays.csv")

# Production Ready Way:
today_bdays = df[(df["month"] == current_dt.month) & (df["day"] == current_dt.day)]
if not today_bdays.empty:
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)

            for index, bday_person in today_bdays.iterrows():
                name = bday_person["name"]
                target_mail = bday_person["email"]

                template_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
                with open(template_path) as letter_file:
                    letter_content = letter_file.read()
                    letter_content = letter_content.replace("[NAME]", name)

                msg = EmailMessage()
                msg["Subject"] = "HAPPY BIRTHDAY"
                msg["From"] = my_email
                msg["To"] = target_mail
                msg.set_content(letter_content)

                connection.send_message(msg)
                print(f"Birthday email sent to {name} at {target_mail}")
    except Exception as e:
        print(f"Network or SMTP error occurred: {e}")
