def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 55 and i < 66 and (ord(char) > ord('f')) and (ord(char) < ord('|')):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)