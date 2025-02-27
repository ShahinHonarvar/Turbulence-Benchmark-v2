def filter_chars(text):
    filtered = ''
    for char in text:
        if not (37 <= ord(char) <= 56 and 6 <= ord(char) <= 95):
            filtered += char
    return filtered