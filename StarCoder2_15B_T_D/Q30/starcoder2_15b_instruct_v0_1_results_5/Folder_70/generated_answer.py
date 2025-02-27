def insert_before_character(text):
    result = ''
    for i, char in enumerate(text):
        if char == 'P':
            result += 'VP'
        else:
            result += char
    return result