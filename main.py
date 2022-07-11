with open("Input/Names/invited_names.txt") as name_file:
    for name in name_file.readlines():
        stripped_name = name.strip()
        greeting = f"Dear {stripped_name},\n"
        with open("Input/Letters/starting_letter.txt") as text_file:
            text_list = text_file.readlines()
            text_list[0] = greeting
            with open(f"Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as letter_personalised:
                letter_personalised.writelines(text_list)
