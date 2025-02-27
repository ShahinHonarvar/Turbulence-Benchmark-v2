def filter_chars(s):
    chars_to_remove = set([c for c in s[19:23] if ']' <= c <= 't'])
    result = ''.join([c for c in s if c not in chars_to_remove])
    return result