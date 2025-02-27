def filter_chars(s):
    chars = set()
    for i in range(10, 53):
        if '@' <= s[i] <= 'T':
            chars.add(s[i])
    return ''.join((c for c in s if c not in chars))