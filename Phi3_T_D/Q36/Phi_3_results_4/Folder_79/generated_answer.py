def filter_chars(s):
    sub = s[11:46]
    filtered_chars = [c for c in sub if not '!' < c < 'A']
    return s[:11] + ''.join(filtered_chars) + s[46:]