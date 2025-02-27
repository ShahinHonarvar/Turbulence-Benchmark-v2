def filter_chars(s):
    chars_to_remove = set(s[722:833]) & set('KLMnopqrst')
    return ''.join((c for c in s if c not in chars_to_remove))