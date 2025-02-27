def insert_before_character(text):
    result = ''
    for char in text:
        result += char
        if char == '4':
            result += 'F'
    return result