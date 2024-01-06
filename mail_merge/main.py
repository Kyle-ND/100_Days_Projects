#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./mail_merge/Input/Names/invited_names.txt') as file_of_names:
    names = file_of_names.readlines()
    with open('./mail_merge/Input/Letters/starting_letter.docx') as letter_template:
        letter = letter_template.read()
        for i in names:
            name = i.strip()
            with open(f"./mail_merge/Output/ReadyToSend/letter_for_{name}.docx", 'w') as invite:
                invite.write(letter.replace('[name]',name))
