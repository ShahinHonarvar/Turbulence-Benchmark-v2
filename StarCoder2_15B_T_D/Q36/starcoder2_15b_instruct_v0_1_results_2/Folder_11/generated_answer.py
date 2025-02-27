def filter_chars(string: str) -> str:
    filtered_string = ''
    for char in string:
        if not (86 < ord(char) < 93 and char > 'E' and (char < '~')):
            filtered_string += char
    return filtered_string