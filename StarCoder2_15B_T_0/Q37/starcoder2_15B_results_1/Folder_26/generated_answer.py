def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'i' or char > 'k' or string.index(char) < 20 or (string.index(char) > 62):
            filtered_chars.append(char)
    return ''.join(filtered_chars)