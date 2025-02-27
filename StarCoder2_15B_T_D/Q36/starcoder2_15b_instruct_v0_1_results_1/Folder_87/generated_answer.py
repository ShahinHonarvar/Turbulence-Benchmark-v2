def filter_chars(text):
    filtered = ''
    for c in text:
        if not (32 < ord(c) < 61 and '3' < c < 'D'):
            filtered += c
    return filtered