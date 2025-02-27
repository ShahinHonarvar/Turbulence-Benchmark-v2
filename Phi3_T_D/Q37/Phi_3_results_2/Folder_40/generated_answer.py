def filter_chars(s):
    first_two = s[:2]
    char_to_filter = [c for c in first_two if '*' <= c <= 's']
    for ch in char_to_filter:
        s = s.replace(ch, '')
    return s