def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'H':
            result += 'sH'
        else:
            result += char
    return result