def insert_before_character(string):
    result = ''
    for char in string:
        result += char
        if char == 'I':
            result += 'I'
    return result