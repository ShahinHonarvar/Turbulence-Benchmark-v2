def filter_chars(text):
    filtered = ''
    for char in text:
        if not (33 <= ord(char) <= 70 and 7 <= char <= 'k'):
            filtered += char
    return filtered