def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'g':
            result += 't'
        result += char
    return result