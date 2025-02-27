def insert_before_character(string):
    result = ''
    for char in string:
        if char == '6':
            result += 'W6'
        else:
            result += char
    return result