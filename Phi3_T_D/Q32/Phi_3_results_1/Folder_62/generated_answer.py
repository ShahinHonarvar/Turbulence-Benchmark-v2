def insert_after_character(text):
    result = ''
    for char in text:
        if char == ' ':
            result += 'o' + char
        else:
            result += char
    return result