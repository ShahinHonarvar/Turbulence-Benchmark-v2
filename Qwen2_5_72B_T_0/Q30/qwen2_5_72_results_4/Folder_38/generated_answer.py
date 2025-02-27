def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'X':
            result += '6X'
        else:
            result += char
    return result