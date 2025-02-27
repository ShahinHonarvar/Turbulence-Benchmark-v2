def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'e':
            result += 'e' + char
        else:
            result += char
    return result