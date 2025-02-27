def filter_chars(s):
    chars_to_remove = set()
    for i in range(521, 723):
        if 52 <= ord(s[i]) <= 95:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))