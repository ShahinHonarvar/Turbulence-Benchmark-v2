def filter_chars(s):
    remove_chars = set()
    for i in range(21, 25):
        if '5' < s[i] < '}':
            remove_chars.add(s[i])
    return ''.join((c for c in s if c not in remove_chars))