def insert_before_character(text):
    result = ''
    for char in text:
        if char == ' ' and 'P' not in result:
            result += 'P'
        result += char
    return result