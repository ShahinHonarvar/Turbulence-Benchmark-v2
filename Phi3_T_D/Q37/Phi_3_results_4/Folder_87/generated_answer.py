def filter_chars(s):
    filtered_chars = [c for i, c in enumerate(s[17:82], start=18) if 'W' <= c <= '[']
    for char in filtered_chars:
        s = s.replace(char, '')
    return s