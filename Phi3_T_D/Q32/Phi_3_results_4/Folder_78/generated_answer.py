def insert_after_character(text):
    result = ''
    for char in text:
        if char == 'H':
            result += 's' + char
        else:
            result += char
    return result