def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 38 or i > 99 or char < 'A' or (char > 'Q'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)