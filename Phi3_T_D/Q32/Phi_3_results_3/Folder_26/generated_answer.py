def insert_after_character(text):
    result = ''
    after_r = False
    for char in text:
        result += char
        if after_r and char not in ('', 'r'):
            result += 'w'
        if char == 'r':
            after_r = True
        else:
            after_r = False
    return result