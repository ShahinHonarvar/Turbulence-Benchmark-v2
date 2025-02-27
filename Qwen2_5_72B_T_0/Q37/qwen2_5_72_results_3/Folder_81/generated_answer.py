def filter_chars(s):
    chars_to_remove = set()
    for i in range(19, 93):
        if 19 <= i <= 92 and '8' <= s[i] <= 'm':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result