def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 3 and i < 9 and (ord(char) > ord('*')) and (ord(char) < ord('E')):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)