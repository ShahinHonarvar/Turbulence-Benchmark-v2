def insert_before_character(s):
    new_str = ''
    for char in s:
        if char == 'O':
            new_str += 'O'
        new_str += char
    return new_str