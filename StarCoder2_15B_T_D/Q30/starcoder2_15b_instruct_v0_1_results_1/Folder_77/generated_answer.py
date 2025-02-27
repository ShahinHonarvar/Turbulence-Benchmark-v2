def insert_before_character(string):
    result = ''
    for i, char in enumerate(string):
        if char == '9':
            result += 'h9'
        else:
            result += char
    return result