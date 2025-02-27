def filter_chars(s):
    chars_to_remove = set()
    for i in range(43, 81):
        if 44 <= i <= 80 and '=' <= s[i] <= 'E':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result