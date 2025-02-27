def insert_before_character(s):
    result = ''
    for c in s:
        if c == 'w':
            result += 'n'
        result += c
    return result