def filter_chars(s):
    chars_to_remove = set()
    for i in range(503, 754):
        if 57 <= ord(s[i]) <= 119:
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result