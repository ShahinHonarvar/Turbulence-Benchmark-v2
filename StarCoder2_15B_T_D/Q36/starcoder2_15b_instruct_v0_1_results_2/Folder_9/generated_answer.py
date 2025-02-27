def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 50 or i >= 92 or (not 'A' < char < 'Q'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)