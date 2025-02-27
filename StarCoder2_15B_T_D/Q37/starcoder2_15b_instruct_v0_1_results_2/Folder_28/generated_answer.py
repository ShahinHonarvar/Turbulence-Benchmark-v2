def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (20 <= ord(char) <= 79 and ord('!') <= ord(char) <= ord('T')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)