def insert_before_character(string):
    result = ''
    for char in string:
        if char == ' ':
            result += '5'
        result += char
    return result