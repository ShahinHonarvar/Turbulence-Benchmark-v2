def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (5 <= ord(char) - ord('A') <= 6 and 'G' <= char <= 'p'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)