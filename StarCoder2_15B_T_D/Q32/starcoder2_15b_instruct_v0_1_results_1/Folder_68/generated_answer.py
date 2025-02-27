def insert_after_character(text: str) -> str:
    output = []
    for character in text:
        output.append(character)
        if character == 'i':
            output.append('0')
    return ''.join(output)