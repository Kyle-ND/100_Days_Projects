import smtplib
import random
from datetime import datetime

def sender(message):
# Sender email creds
    admin_email = "teamcodeclinics@gmail.com"
    password = "npfekqklfoafhexm"

    # starting server and connecting to gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(admin_email,password)

        server.sendmail(from_addr=admin_email,to_addrs='franciscakapenda@gmail.com',msg=f'Subject: Monday Motivation\n\n{message}')

def get_qoutes():
    with open('qoutes.txt') as file:
        qoutes = file.readlines()
        return qoutes

def day_checker():

    weekdays = ["monday","tuesday","wednesday","thursday","friday"]
    today_date = datetime.now()
    week_day = weekdays[today_date.weekday()].title()
    qoute = random.choice(get_qoutes())

    if week_day == "Monday":
        msg = f"\nToday is {week_day}\n\n{qoute}\n\n have a great week :)"
        sender(msg)
        print("email sent")
    else:
        print("The week has already began keep pushing through :)")



if __name__ == "__main__":
    day_checker()