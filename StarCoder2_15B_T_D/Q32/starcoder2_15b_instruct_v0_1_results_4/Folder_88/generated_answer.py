def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'a':
            result += 'at'
        else:
            result += c
    return result