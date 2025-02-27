def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'N':
            result += 'jN'
        else:
            result += char
    return result