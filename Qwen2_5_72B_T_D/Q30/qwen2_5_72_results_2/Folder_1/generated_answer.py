def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'U':
            result += 'TU'
        else:
            result += char
    return result