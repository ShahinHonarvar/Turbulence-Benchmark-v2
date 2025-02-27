def filter_chars(s):
    subset = s[170:195]
    chars_to_remove = [c for c in subset if '!' < c < '}']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s