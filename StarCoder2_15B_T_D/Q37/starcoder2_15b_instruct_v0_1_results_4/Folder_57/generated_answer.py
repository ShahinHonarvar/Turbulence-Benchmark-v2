def filter_chars(string):
    filtered_chars = []
    for char in string:
        if (char < '!' or char > 'B') or (string.index(char) < 27 or string.index(char) > 85):
            filtered_chars.append(char)
    return ''.join(filtered_chars)