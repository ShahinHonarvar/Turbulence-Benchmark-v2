def filter_chars(s):
    chars_to_remove = set()
    for i in range(4, 8):
        if '1' < s[i] < 'J':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result