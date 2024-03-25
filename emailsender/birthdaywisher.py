import smtplib
import csv
import random
from datetime import datetime

num = random.randint(1,3)
def get_birthdays():
    with open("birthdays.csv") as f:
        data = csv.DictReader(f)
        return data
    
def sender(message):
# Sender email creds
    admin_email = "teamcodeclinics@gmail.com"
    password = "npfekqklfoafhexm"

    # starting server and connecting to gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(admin_email,password)

        server.sendmail(from_addr=admin_email,to_addrs='kkndlovu9@gmail.com',msg=f'Subject: Happy Birthday!\n\n{message}')

def message_creator():

    today_date = datetime.now()
    today_day = today_date.day
    current_month = today_date.month
   
    with open("birthdays.csv") as f:
        people = csv.DictReader(f)

        for person in people:

            if int(person['month']) == current_month:
                print("There is a birthday this month")
                if int(person['day']) == today_day:
                    print("Birth day found today")
                    print("sending email......")
                    with open(f"letter_templates/letter_{num}.txt") as temp:
                        mess = temp.read()
                        sender(mess.replace('[NAME]',person['name']))
                    
                else:
                    print("No birthdays today")
        print("No birthdays found this month")

if __name__ == "__main__":
    message_creator()