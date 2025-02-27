def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 24 and i < 37 and (ord(char) > ord('A')) and (ord(char) < ord('h')):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)