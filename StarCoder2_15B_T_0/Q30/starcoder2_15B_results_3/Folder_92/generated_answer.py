def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'a':
            result += 'a'
        result += c
    return result