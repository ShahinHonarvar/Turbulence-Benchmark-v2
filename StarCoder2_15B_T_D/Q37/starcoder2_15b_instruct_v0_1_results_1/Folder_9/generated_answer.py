def filter_chars(string):
    filtered = ''
    for char in string:
        if not 38 <= ord(char) - ord('A') <= 61:
            filtered += char
    return filtered