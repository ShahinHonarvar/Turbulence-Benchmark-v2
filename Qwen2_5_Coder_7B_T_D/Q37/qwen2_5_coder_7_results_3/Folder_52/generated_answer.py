def filter_chars(s):
    chars_to_keep = [c for c in s if not (54 <= s.index(c) <= 83 and 'j' <= c <= 'v')]
    return ''.join(chars_to_keep)