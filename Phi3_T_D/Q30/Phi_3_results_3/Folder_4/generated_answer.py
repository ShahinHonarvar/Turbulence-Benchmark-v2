def insert_before_character(s):
    result = ''
    for char in s:
        if char.lower() == 'a':
            result += '6' + char
        else:
            result += char
    return result