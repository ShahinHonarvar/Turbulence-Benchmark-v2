def insert_after_character(string):
    result = ''
    for char in string:
        if char == 'C':
            result += 'CH'
        else:
            result += char
    return result