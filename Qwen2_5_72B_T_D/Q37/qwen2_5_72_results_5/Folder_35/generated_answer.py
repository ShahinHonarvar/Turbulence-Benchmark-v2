def filter_chars(s):
    remove_chars = set()
    for i in range(155, 404):
        if 0 <= i < len(s) and '(' <= s[i] <= ']':
            remove_chars.add(s[i])
    result = ''.join((c for c in s if c not in remove_chars))
    return result