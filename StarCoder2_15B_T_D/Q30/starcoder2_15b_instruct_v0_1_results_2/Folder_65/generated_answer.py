def insert_before_character(string):
    result = ''
    for char in string:
        if char == '6':
            result += '96'
        else:
            result += char
    return result