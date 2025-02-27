def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if not (i > 10 and i < 46 and ('!' < char < 'A')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)