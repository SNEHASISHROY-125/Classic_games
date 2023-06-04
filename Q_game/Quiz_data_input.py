import save_Q_data_input
Question_dict = {}
Q_no = 0
How_many_Q = int(input('How many do you want to create? \n> '))

def data_input():
    Q_x = {}  # Create a new empty dictionary for each question
    question = input('Type your question > ').upper()
    type = input('Set mode: \nMCQ/T-F/FILL_IN_THE_BLANKS\n> ').upper()
    options = []
    keys = ['A', 'B', 'C', 'D']

    if type == 'MCQ':
        for i in keys:
            options.append(input(f'Set options\n{i} > ').upper())
        answer = input('Correct Answer [A/B/C/D]\n').upper()
        Q_options = dict(zip(keys, options))
        Q_x[f'Question{Q_no}'] = question
        Q_x['Type'] = type
        Q_x['Options'] = Q_options
        Q_x['Answer'] = answer

    elif type == 'FILL_IN_THE_BLANKS':
        answer = input('Correct Answer "____"\n').upper()
        Q_x[f'Question{Q_no}'] = question
        Q_x[f'Type'] = type
        Q_x['Answer'] = answer

    elif type == 'T-F':
        answer = input('Correct Answer [T/F]\n').upper()
        option = {
            'A': 'T',
            'B': 'F'
        }
        Q_x[f'Question{Q_no}'] = question
        Q_x['Type'] = type
        Q_x['Options'] = option
        Q_x['Answer'] = answer

    return Q_x

while Q_no < How_many_Q:
    Q_no += 1
    data_as_dict = data_input()
    Question_dict[f'Q.{Q_no}'] = data_as_dict

# File name input:
file_name = input('Save file as: ')
# Save Dict as txt file:
save_Q_data_input.save_as_file(Question_dict , file_name)

