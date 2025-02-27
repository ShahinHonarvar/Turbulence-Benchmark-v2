def insert_before_character(string):
    result = ''
    for i, char in enumerate(string):
        if char == 'r':
            result += 'w'
        result += char
    return result