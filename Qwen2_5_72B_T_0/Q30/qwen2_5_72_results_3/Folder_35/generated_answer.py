def insert_before_character(s):
    result = ''
    for char in s:
        if char == '9':
            result += 'M9'
        else:
            result += char
    return result