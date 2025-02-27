def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= '8' or char >= 'm':
            filtered_chars.append(char)
    return ''.join(filtered_chars)