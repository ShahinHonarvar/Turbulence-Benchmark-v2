def insert_before_character(s):
    result = ''
    for char in s:
        if char == '2':
            result += 'S' + char
        else:
            result += char
    return result