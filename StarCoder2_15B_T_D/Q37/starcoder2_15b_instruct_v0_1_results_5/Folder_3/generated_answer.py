def filter_chars(s):
    filtered = ''
    for char in s:
        if not (37 <= ord(char) <= 56 and 6 <= ord(char) <= 95):
            filtered += char
    return filtered