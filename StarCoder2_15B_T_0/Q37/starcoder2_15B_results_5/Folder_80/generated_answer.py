def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'a' or char > 'i':
            filtered_chars.append(char)
    return ''.join(filtered_chars)