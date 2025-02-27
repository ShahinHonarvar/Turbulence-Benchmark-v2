def filter_chars(s):
    remove_chars = set()
    for i in range(49, 56):
        if 'I' < s[i] < 'a':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result