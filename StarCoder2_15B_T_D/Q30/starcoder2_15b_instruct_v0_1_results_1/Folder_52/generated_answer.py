def insert_before_character(text):
    result = ''
    for char in text:
        result += char
        if char == 'T':
            result += 'V'
    return result