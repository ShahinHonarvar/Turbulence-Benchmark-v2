def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not 10 <= ord(char) - ord('I') <= 59:
            filtered_chars.append(char)
    return ''.join(filtered_chars)