def insert_after_character(s):
    result = ''
    for char in s:
        result += char
        if char == 'X':
            result += '6'
    return result