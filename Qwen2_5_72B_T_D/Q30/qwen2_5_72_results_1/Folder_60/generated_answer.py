def insert_before_character(s):
    result = ''
    for char in s:
        if char == 'C':
            result += 'PC'
        else:
            result += char
    return result