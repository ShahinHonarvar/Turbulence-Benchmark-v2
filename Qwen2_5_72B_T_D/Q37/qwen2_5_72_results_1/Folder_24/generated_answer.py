def filter_chars(s):
    remove_chars = set()
    for i in range(36, 80):
        if '2' <= s[i] <= 's':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result