def insert_after_character(string):
    result = ''
    for char in string:
        if char == 'P':
            result += 'V'
        result += char
    return result