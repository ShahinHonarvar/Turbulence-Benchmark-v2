def insert_before_character(text):
    result = ''
    for char in text:
        result += 'u' + char if char == 'u' else char
    return result