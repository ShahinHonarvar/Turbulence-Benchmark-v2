def filter_chars(s):
    chars_to_remove = set()
    for i in range(11, 33):
        if '!' <= s[i] <= '@':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result