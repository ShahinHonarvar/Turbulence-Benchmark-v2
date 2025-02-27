def insert_before_character(string):
    result = ''
    for char in string:
        if char == 'j':
            result += 'q'
        result += char
    return result