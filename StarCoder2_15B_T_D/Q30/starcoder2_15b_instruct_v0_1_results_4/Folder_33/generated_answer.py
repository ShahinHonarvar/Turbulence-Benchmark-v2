def insert_before_character(string: str) -> str:
    output = ''
    for i, c in enumerate(string):
        if c == 'a':
            output += 'n'
        output += c
    return output