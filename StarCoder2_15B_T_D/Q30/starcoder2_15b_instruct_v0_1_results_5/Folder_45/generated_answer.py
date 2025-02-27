def insert_before_character(text):
    output = ''
    for i, c in enumerate(text):
        if c == 'O':
            output += 'O'
        output += c
    return output