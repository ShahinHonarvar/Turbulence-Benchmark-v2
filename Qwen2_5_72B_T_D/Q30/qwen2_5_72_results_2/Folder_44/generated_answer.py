def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'g':
            result += 'M' + char
        else:
            result += char
    return result