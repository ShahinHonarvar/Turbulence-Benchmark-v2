def insert_before_character(string):
    result = ''
    for i, char in enumerate(string):
        if char == 'S':
            result += 'US'
        else:
            result += char
    return result