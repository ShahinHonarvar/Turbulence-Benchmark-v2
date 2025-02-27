def filter_chars(s):
    remove_chars = set()
    for i in range(36, 41):
        if 'H' <= s[i] <= 'e':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result