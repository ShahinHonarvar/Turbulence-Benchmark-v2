def insert_before_character(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] == 'a':
            new_string += 'a'
        new_string += string[i]
    return new_string