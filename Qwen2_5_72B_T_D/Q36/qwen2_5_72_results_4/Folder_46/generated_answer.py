def filter_chars(s):
    chars_to_remove = set()
    for i in range(19, 69):
        if 'E' > s[i] > '<':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result