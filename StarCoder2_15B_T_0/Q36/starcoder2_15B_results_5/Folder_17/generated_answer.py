def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'K' or char >= 'a':
            filtered_chars.append(char)
    return ''.join(filtered_chars)