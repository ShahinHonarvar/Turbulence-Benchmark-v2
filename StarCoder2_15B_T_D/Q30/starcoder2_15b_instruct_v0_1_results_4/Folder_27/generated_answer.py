def insert_before_character(text):
    result = ''
    for i, c in enumerate(text):
        if c == 'N':
            result += 'j'
        result += c
    return result