def insert_before_character(input_string):
    index = input_string.find('r')
    if index != -1:
        return input_string[:index] + 'w' + input_string[index:]
    else:
        return input_string