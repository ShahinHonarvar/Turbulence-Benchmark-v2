def insert_before_character(s):
    result = ''
    for char in s:
        if char == '6':
            result += 'W6'
        else:
            result += char
    return result