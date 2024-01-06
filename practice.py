# # list comprehension
# import random
# numbers = [1,2,3]
# new_list = [n+1 for n in numbers]

# name = "Angela"
# new_list = [letter for letter in name]

# ran = range(1,5)
# new_ran = [n * 2 for n in ran]

# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# short_names = [n.upper() for n in names if len(n) >= 5]

# nums = [1,1,2,3,5,8,13,21,34,55]
# new_nums = [n  for n in nums if n % 2 == 0]

# #dict comprehension
# #new_dict = {new_key:new_value for (key,vale) in dict.items()}

# names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
# student_score = {name:random.randint(10,99) for name in names}
# # print(student_score)
# passed_students = {key:value for (key,value) in student_score.items() if value > 50}
# # print(passed_students)

# weather = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# ferinhiegth = {key:(value*9/5) + 32 for (key,value) in weather.items()}
# print(ferinhiegth)

import tkinter as tk
window = tk.Tk()
window.title("PYTHON GUI")
window.minsize(600,400)
label = tk.Label(text="Welcome To SP",font=("Arial",15,"bold"))
label.pack()
def main():
    button = tk.Button(text="Login",command=login)
    button.pack()

    window.mainloop()

def login():
    username = tk.Entry()
    username.pack()
    password = tk.Entry()
    password.pack()
    label.config(text="Logged In...")

if __name__ == "__main__":
    main()

# def add(*nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum 


# res = add(1,23,4)

# print(res)
