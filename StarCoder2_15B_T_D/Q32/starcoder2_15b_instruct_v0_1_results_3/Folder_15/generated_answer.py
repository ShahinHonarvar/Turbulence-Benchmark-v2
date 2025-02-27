def insert_after_character(s: str) -> str:
    output = ''
    for char in s:
        if char == 'o':
            output += 'oo'
        else:
            output += char
    return output