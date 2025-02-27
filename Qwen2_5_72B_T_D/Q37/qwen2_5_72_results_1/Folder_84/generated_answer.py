def filter_chars(s):
    chars_to_remove = set()
    for i in range(138, 921):
        if 138 <= i <= 920 and '6' <= s[i] <= 'A':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result