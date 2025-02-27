def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'g':
            result += 'tg'
        else:
            result += char
    return result