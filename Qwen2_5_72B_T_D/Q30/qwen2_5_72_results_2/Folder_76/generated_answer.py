def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'F':
            result += 'm'
        result += char
    return result