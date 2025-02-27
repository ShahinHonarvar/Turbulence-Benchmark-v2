def insert_before_character(string):
    result = ''
    for char in string:
        result += char
        if char == '6':
            result += '9'
    return result