def insert_before_character(s):
    result = ''
    for char in s:
        if char == '5':
            result += 'h' + char
        else:
            result += char
    return result