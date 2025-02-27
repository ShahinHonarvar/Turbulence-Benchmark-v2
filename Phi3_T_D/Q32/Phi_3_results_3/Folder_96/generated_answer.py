def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'a':
            result += 'aA'
        else:
            result += char
    return result