def filter_chars(s):
    filtered_chars = [c for c in s[42:68] if 't' < c < 'x']
    return s.translate(str.maketrans('', '', ''.join(filtered_chars)))