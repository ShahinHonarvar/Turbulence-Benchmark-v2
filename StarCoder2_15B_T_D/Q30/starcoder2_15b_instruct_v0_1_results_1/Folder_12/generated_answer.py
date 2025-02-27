def insert_before_character(text: str) -> str:
    result = ''
    for i, c in enumerate(text):
        if c == 'I':
            result += ' '
        result += c
    return result