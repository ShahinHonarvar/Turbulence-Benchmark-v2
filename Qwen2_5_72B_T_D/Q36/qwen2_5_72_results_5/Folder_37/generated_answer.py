def filter_chars(s):
    remove_chars = set()
    for i in range(44, 59):
        if '/' < s[i] < '6':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result