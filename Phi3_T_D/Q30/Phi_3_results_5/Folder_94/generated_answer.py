def insert_before_character(text):
    result = ''
    for char in text:
        if char == ' ':
            result += '5'
        result += char
    return result