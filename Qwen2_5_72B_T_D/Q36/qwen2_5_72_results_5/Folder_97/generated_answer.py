def filter_chars(s):
    chars_to_remove = set()
    for i in range(309, 591):
        if 309 <= i < 591 and 'S' < s[i] < 'm':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result