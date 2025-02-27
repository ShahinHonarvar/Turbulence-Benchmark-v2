def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'j':
            result += '1j'
        else:
            result += char
    return result