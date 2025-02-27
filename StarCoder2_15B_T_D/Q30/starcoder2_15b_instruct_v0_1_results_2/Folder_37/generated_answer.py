def insert_before_character(string):
    result = ''
    for i in range(len(string)):
        if string[i] == 'U':
            result += 'aU'
        else:
            result += string[i]
    return result