def filter_chars(s):
    chars_to_remove = {c for c in s[603:760] if 'Q' <= c <= 'h'}
    return ''.join((c for c in s if c not in chars_to_remove))