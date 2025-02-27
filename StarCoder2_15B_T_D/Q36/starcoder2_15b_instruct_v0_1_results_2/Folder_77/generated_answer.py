def filter_chars(string: str) -> str:
    new_string = ''
    for char in string:
        if not 221 < ord(char) < 419:
            new_string += char
    return new_string