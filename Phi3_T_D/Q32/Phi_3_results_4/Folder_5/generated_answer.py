def insert_after_character(s):
    result = ''
    for char in s:
        if char == 'c':
            result += char + 'G'
        else:
            result += char
    return result