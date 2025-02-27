def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'r':
            result += 'w'
    return result