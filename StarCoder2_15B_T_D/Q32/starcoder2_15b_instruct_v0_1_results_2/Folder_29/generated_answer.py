def insert_after_character(text):
    result = ''
    for c in text:
        result += c
        if c == 'N':
            result += 'z'
    return result