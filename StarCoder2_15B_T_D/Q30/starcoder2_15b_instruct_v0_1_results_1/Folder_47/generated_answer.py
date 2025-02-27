def insert_before_character(text):
    new_text = ''
    for i, c in enumerate(text):
        if c == 'E':
            new_text += 'f'
        new_text += c
    return new_text