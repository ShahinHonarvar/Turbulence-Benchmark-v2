def insert_after_character(s):
    result = ''
    for char in s:
        result += char
        if char == 'A':
            result += 'H'
    return result