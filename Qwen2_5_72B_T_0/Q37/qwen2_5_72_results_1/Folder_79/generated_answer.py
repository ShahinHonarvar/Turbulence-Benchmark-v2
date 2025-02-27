def filter_chars(s):
    chars_to_remove = set()
    for i in range(10, 53):
        if 10 <= i <= 52 and '@' <= s[i] <= 'T':
            chars_to_remove.add(s[i])
    result = ''.join((c for c in s if c not in chars_to_remove))
    return result