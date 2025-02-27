def filter_chars(s):
    remove_chars = set()
    for i in range(20, 63):
        if 20 <= i < len(s) and 'i' <= s[i] <= 'k':
            remove_chars.add(s[i])
    return ''.join((c for c in s if c not in remove_chars))