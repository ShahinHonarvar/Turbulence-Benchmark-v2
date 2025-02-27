def filter_chars(s):
    chars_to_remove = set()
    for i in range(83, 100):
        char = s[i]
        if '*' <= char <= 'j':
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))