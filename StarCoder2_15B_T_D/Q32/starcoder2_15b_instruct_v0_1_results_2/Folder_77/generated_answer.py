def insert_after_character(string: str) -> str:
    output = []
    for i, c in enumerate(string):
        output.append(c)
        if c == '9':
            output.append('h')
    return ''.join(output)