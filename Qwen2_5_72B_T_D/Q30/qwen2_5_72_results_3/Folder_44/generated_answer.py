def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'g':
            result += 'M'
        result += char
    return result