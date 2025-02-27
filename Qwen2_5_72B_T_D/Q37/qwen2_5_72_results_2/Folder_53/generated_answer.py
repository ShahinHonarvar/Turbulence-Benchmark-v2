def filter_chars(s):
    chars_to_remove = set()
    for i in range(83, 100):
        if 83 <= i <= 99 and '*' <= s[i] <= 'j':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result