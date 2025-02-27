def insert_before_character(string):
    result = ''
    for i, c in enumerate(string):
        if c == 'A':
            result += 'a'
        result += c
    return result