def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 2 or i >= 7:
            filtered_chars.append(char)
        elif not (ord(char) > ord('h') and ord(char) < ord('k')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)