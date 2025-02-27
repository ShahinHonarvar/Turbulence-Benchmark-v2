def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not 4 <= ord(char) - ord('0') <= 14:
            filtered_chars.append(char)
    return ''.join(filtered_chars)