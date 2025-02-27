def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '+' or char > '8' or string.index(char) < 21 or (string.index(char) > 43):
            filtered_chars.append(char)
    return ''.join(filtered_chars)