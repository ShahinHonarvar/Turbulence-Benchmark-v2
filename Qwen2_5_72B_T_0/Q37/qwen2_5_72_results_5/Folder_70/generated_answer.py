def filter_chars(s):
    to_remove = set()
    for i in range(515, 539):
        if 515 <= i < len(s) and '+' <= s[i] <= '}':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result