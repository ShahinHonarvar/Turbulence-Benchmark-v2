def filter_chars(s):
    remove_chars = set()
    for i in range(225, 382):
        if 225 <= i <= 381 and 'D' <= s[i] <= 'Y':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result