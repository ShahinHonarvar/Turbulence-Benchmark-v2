def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'U':
            result += 'uU'
        else:
            result += char
    return result

def insert_before_character(string):
    return ''.join(['uU' if char == 'U' else char for char in string])