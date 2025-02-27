def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not 11 <= ord(char) - ord('i') <= 51:
            filtered_chars.append(char)
    return ''.join(filtered_chars)