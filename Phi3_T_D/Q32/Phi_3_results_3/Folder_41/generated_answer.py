def insert_after_character(text):
    result = ''
    i = 0
    while i < len(text):
        if text[i] == 'O':
            result += 'Oo'
        else:
            result += text[i]
        i += 1
    return result