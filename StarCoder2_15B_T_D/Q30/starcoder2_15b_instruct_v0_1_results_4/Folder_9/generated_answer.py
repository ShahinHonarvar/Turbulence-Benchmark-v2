def insert_before_character(string):
    result = ''
    for i, char in enumerate(string):
        if char == 'e':
            result += 'E'
        result += char
    return result