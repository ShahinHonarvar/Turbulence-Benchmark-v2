def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= '7' or char >= 'H':
            filtered_chars.append(char)
    return ''.join(filtered_chars)