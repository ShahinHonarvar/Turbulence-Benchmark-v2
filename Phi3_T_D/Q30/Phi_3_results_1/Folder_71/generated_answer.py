def insert_before_character(text):
    result = ''
    for character in text:
        if character == '2':
            result += 'S'
        result += character
    return result