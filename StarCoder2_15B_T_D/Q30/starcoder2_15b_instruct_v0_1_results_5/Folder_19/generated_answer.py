def insert_before_character(s):
    result = ''
    for i, c in enumerate(s):
        if c == '5':
            result += 'h'
        result += c
    return result