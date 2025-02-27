def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'O':
            result += 'Q'
        result += char
    return result