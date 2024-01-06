# import requests
# import sys

# response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# rate = response.json()
# print(f"${rate['bpi']['USD']['rate']}")


def main():
    import re 

    duration_session = 4
    #get email and current time and frmat the time 
    email = input("enter your email: ")

    #vaidate email and log user in 
    match = re.match(r"^\w+@Student.Wethinkcode.co.za$",email,re.IGNORECASE)
    if match:
        print("logged in")
        session()
    else:
        print("you don't learn at wethinkcode")


def session():
    import datetime

    # Set the session duration (in hours)
    session_duration = 30

    # Get the current time
    start_time = datetime.datetime.now()

    # Calculate the end time
    end_time = start_time + datetime.timedelta(seconds=session_duration)

    # Print the start and end times for reference
    print("Session started at:", start_time)
    print("Session will end at:", end_time)

    # Continuously check the time until the session ends
    while datetime.datetime.now() < end_time:
        # Get the remaining time
        remaining_time = end_time - datetime.datetime.now()

        # Format the remaining time as hours, minutes, and seconds
        hours = remaining_time.seconds // 3600
        minutes = (remaining_time.seconds % 3600) // 60
        seconds = remaining_time.seconds % 60
        


if __name__ == "__main__":
    main()
