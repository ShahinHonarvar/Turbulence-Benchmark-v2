def insert_before_character(s):
    result = ''
    for i, c in enumerate(s):
        if c == 'r':
            result += 'w'
        result += c
    return result