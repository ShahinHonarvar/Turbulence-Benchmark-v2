def filter_chars(s):
    filtered = ''
    for c in s:
        if not 46 <= ord(c) <= 85 or (ord(c) < ord('-') or ord(c) > ord('X')):
            filtered += c
    return filtered