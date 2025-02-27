def insert_before_character(string):
    result = ''
    for char in string:
        if char == '4':
            result += 'F'
        result += char
    return result