def insert_after_character(s):
    result = ''
    for char in s:
        result += char
        if char == 'a':
            result += '0'
    return result