def insert_after_character(s):
    result = ''
    for char in s:
        if char == '2':
            result += '2S'
        else:
            result += char
    return result