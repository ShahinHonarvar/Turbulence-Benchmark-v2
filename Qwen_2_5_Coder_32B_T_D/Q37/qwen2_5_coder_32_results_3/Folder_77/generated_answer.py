def filter_chars(s):
    t = s[384:412]
    chars_to_remove = {c for c in t if '/' <= c <= '8'}
    return ''.join((c for c in s if c not in chars_to_remove))