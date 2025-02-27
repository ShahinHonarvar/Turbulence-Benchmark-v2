def insert_after_character(string):
    result = ''
    for i, c in enumerate(string):
        result += c
        if c == 'e':
            result += 'e'
    return result