def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'w':
            result += 'n' + char
        else:
            result += char
    return result