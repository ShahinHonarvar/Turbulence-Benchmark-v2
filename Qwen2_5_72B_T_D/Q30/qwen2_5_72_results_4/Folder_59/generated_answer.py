def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'o':
            result += '0o'
        else:
            result += char
    return result