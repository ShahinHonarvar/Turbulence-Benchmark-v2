def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'O':
            result += 'jO'
        else:
            result += char
    return result