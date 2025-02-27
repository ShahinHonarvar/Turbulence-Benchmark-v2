def filter_chars(string: str) -> str:
    filtered_string = ''
    for char in string:
        if not ',' < char < 'f':
            filtered_string += char
    return filtered_string