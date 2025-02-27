def filter_chars(string: str) -> str:
    for i in range(52, 82):
        char = string[i]
        if char.isascii() and char.isupper():
            string = string.replace(char, '')
    return string