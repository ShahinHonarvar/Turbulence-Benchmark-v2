def insert_before_character(s):
    result = ''
    for char in s:
        if char == '9':
            result += 'h' + char
        else:
            result += char
    return result