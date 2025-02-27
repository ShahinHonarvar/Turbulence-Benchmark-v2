def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'N':
            result += 'zN'
        else:
            result += char
    return result