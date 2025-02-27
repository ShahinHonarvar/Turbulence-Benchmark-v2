def insert_after_character(text):
    output = []
    for char in text:
        output.append(char)
        if char == 'i':
            output.append('i')
    return ''.join(output)