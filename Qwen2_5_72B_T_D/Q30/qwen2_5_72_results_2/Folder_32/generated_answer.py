def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'F':
            result += 'u'
        result += char
    return result