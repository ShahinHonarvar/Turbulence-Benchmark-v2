def insert_after_character(s: str) -> str:
    output = []
    for char in s:
        if char == '5':
            output.append('h')
        output.append(char)
    return ''.join(output)