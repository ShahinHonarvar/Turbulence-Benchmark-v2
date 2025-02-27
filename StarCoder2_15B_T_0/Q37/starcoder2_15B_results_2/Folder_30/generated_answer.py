def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (41 <= ord(char) <= 64 and ord('K') <= ord(char) <= ord(']')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)