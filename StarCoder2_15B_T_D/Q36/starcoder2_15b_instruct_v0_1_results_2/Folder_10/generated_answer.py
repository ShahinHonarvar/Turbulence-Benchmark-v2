def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 35 and i < 60 and (not '!' < char < 'B'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)