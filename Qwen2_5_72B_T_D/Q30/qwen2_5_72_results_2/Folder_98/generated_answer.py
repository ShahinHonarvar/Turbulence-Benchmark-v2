def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'U':
            result += 'uU'
        else:
            result += char
    return result