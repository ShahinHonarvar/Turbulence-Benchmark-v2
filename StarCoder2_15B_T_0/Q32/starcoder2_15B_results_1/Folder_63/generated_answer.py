def insert_after_character(string):
    result = ''
    for char in string:
        result += char
        if char == '5':
            result += 'R'
    return result