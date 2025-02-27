def filter_chars(s):
    to_remove = set()
    for i in range(42, 78):
        char = s[i]
        if '!' < char < '?':
            to_remove.add(char)
    return ''.join([c for c in s if c not in to_remove])