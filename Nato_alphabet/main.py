import pandas
# getting dataframe by reading from csv
student_data_frame = pandas.read_csv('./Nato_alphabet/nato_phonetic_alphabet.csv')

# converting given dataframe to dict
nato = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}

# getting word from user 
word = input("enter a word: ")

# converting word to nato code
converted_to_nato = [nato[n.upper()] for n in word]

# Displaying nato code
print(converted_to_nato)


