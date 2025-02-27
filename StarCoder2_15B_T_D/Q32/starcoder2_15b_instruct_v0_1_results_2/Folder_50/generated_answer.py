def insert_after_character(string):
    new_string = ''
    for i in range(len(string)):
        new_string += string[i]
        if string[i] == 't':
            new_string += 'u'
    return new_string