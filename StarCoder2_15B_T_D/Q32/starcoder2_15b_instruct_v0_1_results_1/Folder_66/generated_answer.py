def insert_after_character(text: str) -> str:
    output = ''
    for char in text:
        output += char
        if char == 'k':
            output += 'k'
    return output