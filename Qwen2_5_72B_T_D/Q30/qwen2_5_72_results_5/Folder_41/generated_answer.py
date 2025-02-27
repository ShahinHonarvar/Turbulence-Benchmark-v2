def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'O':
            result += 'oO'
        else:
            result += char
    return result