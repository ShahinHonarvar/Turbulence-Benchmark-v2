def filter_chars(s):
    filtered_chars = []
    for char in s:
        if not 1 <= ord(char) - ord('$') <= 5:
            filtered_chars.append(char)
    return ''.join(filtered_chars)