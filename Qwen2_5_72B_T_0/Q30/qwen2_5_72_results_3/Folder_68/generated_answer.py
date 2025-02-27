def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'i':
            result += '0' + char
        else:
            result += char
    return result