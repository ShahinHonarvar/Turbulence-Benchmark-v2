def filter_chars(s):
    chars_to_remove = set()
    for i in range(42, 68):
        if 't' < s[i] < 'x':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))