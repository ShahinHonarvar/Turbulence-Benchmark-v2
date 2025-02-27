def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'S':
            result += 'US'
        else:
            result += char
    return result