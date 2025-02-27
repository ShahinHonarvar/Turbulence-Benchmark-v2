def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'm':
            result += 'N' + char
        else:
            result += char
    return result