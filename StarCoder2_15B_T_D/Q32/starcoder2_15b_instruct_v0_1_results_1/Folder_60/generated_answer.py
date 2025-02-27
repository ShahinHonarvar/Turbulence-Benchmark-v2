def insert_after_character(string: str) -> str:
    output = ''
    for char in string:
        output += char
        if char == 'C':
            output += 'P'
    return output