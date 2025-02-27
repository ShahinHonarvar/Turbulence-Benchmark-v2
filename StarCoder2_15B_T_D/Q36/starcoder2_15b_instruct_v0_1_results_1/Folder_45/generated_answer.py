def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 81 and i < 86 and (not '!' < char < 's'):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)