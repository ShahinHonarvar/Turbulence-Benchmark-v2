def filter_chars(s):
    chars_to_remove = set()
    for i in range(52, 88):
        if 38 < ord(s[i]) < 99:
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result