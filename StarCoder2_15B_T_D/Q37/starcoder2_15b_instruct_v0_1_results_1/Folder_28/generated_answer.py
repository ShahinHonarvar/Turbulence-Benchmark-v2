def filter_chars(string):
    filtered = ''
    for char in string:
        if not 20 <= ord(char) - ord('!') <= 59:
            filtered += char
    return filtered