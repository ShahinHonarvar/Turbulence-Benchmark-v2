def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'Y':
            result += '4Y'
        else:
            result += char
    return result