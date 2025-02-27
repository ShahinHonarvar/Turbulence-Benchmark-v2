def filter_chars(s):
    chars_to_remove = []
    for i, c in enumerate(s):
        if 8 <= i <= 9 and 'R' <= c <= 't':
            chars_to_remove.append(c)
    return ''.join((c for c in s if c not in chars_to_remove))