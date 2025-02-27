def filter_chars(s):
    chars_to_remove = set()
    for i in range(69, 81):
        if 'a' <= s[i] <= 'p':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result