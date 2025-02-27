def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'K':
            result += 'l' + char
        else:
            result += char
    return result