def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 421 or i >= 854:
            filtered_chars.append(char)
        elif not (ord(char) > ord('D') and ord(char) < ord('J')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)