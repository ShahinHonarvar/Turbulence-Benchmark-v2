def insert_after_character(text):
    output = ''
    for i in range(len(text)):
        output += text[i]
        if text[i] == 'O':
            output += 'O'
    return output