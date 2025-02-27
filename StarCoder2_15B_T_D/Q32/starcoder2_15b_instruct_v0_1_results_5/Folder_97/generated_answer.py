def insert_after_character(s):
    result = ''
    for i, c in enumerate(s):
        result += c
        if c == 'o':
            result += 'h'
    return result