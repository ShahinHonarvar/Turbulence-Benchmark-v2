def insert_before_character(text):
    result = ''
    for char in text:
        if char == 'U':
            result += 'a' + char
        else:
            result += char
    return result