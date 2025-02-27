def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i >= 31 and i < 73 and (not (ord(char) > ord('M') and ord(char) < ord('j'))):
            filtered_chars.append(char)
    return ''.join(filtered_chars)