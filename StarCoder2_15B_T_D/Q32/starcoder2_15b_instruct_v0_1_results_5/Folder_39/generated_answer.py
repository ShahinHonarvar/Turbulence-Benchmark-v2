def insert_after_character(s: str) -> str:
    output = []
    for c in s:
        output.append(c)
        if c == 'm':
            output.append('Q')
    return ''.join(output)