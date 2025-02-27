def insert_before_character(string):
    result = ''
    for char in string:
        if char == '0':
            result += '40'
        else:
            result += char
    return result