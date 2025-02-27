def insert_before_character(s):
    result = ''
    for char in s:
        if char == '0':
            result += ' ' + char
        else:
            result += char
    return result