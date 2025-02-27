def filter_chars(string):
    filtered = ''
    for char in string:
        if char < '!' or char > 's' or 86 <= ord(char) - ord('!') <= 92:
            filtered += char
    return filtered