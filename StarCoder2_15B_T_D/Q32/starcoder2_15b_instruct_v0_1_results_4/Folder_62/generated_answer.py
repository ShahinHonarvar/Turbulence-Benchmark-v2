def insert_after_character(text):
    result = ''
    for character in text:
        result += character
        if character == ' ':
            result += 'o'
    return result