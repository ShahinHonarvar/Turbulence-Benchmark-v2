def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'a':
            result += '0a'
        else:
            result += char
    return result