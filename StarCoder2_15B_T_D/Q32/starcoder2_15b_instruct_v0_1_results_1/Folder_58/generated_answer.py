def insert_after_character(string):
    result = ''
    for i, char in enumerate(string):
        result += char
        if char == 'F':
            result += 'o'
    return result