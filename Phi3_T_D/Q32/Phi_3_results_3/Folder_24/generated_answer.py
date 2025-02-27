def insert_after_character(s):
    result = ''
    for character in s:
        result += character
        if character == '0':
            result += '4'
    return result