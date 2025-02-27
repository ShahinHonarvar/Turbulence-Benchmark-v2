def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'P':
            result += 'V' + char
        else:
            result += char
    return result