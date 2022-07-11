with open("Input/Names/invited_names.txt") as name_file:
    for name in name_file.readlines():
        stripped_name = name.rstrip()
        greeting = f"Dear {stripped_name},\n"
        with open("Input/Letters/starting_letter.txt") as text_file:
            text_list = text_file.readlines()
            text_list[0] = greeting
            with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as letter_personalised:
                letter_personalised.writelines(text_list)


# TODO: Create a letter using starting_letter.txt

# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
