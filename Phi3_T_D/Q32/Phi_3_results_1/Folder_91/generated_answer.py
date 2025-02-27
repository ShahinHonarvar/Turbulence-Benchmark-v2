def insert_after_character(string):
    result = ''
    for char in string:
        if char == 'a':
            result += 'a0'
        else:
            result += char
    return result