def filter_chars(s):
    remove_chars = set()
    for i in range(19, 93):
        if 19 <= i <= 92 and '8' <= s[i] <= 'm':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result