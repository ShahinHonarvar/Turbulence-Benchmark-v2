def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (344 < ord(char) < 874 and ord('f') < ord(char) < ord('~')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)