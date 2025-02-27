def insert_after_character(string):
    result = ''
    for char in string:
        if char == 'o':
            result += 'O'
        result += char
    return result