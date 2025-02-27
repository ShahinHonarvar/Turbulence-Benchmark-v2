def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'j':
            result += 'q'
        result += c
    return result