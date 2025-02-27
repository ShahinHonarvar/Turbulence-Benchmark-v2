def filter_chars(string):
    filtered = ''
    for char in string:
        if not 20 <= ord(char) - ord('i') <= 24:
            filtered += char
    return filtered