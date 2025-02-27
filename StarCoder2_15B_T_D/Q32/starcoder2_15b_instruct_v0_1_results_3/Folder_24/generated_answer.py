def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == '0':
            result += '4'
    return result