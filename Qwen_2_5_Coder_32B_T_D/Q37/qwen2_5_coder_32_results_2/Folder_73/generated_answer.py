def filter_chars(s):
    chars_to_remove = set()
    for i in range(22, 86):
        if 22 <= i < len(s) and '7' <= s[i] <= 'e':
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))