def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'Z' or char >= 'c':
            filtered_chars.append(char)
    return ''.join(filtered_chars)