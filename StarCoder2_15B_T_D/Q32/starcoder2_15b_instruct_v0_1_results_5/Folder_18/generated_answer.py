def insert_after_character(string):
    result = ''
    for i in range(len(string)):
        result += string[i]
        if string[i] == 'K':
            result += 'l'
    return result