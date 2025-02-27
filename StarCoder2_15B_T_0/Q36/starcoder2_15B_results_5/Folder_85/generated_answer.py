def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 55 and i < 80 and (ord(char) > ord('S')) and (ord(char) < ord('s')):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)