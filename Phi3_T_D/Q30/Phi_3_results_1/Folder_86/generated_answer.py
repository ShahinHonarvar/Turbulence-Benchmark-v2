def insert_before_character(text):
    result = ''
    for char in text:
        result += 'Q' if char == 'O' else char
    return result