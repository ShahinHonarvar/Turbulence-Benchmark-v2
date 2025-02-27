def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'a':
            result += 'a0'
        else:
            result += char
    return result