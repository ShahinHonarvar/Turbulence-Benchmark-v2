def insert_before_character(text):
    result = ''
    for i, c in enumerate(text):
        if c == 'E':
            result += 'e'
        result += c
    return result