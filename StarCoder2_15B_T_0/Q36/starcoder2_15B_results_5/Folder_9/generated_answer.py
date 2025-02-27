def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 50 and i < 92 and ('A' < char < 'Q'):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)