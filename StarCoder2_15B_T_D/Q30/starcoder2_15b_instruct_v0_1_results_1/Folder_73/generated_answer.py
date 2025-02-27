def insert_before_character(string):
    result = ''
    for i, char in enumerate(string):
        if char == 'R':
            result += 'V'
        result += char
    return result