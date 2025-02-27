def filter_chars(string: str) -> str:
    for i in range(29, 33):
        if '%' < string[i] < 'a':
            string = string.replace(string[i], '')
    return string