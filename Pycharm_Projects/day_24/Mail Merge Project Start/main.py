PLACEHOLDER="[name]"

with open('./Input/Names/invited_names.txt','r') as names:
    names_list =names.readlines()
#print(names_list)

with open('./Input/Letters/starting_letter.txt') as letter_content:
    letter=letter_content.read()
    for name in names_list:
        stripped_name= name.strip()
        new_letter=letter.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode='w') as completed_letter:
             completed_letter.write(new_letter)

print(new_letter)