def filter_chars(s):
    to_remove = set()
    for i in range(38, 70):
        if 0 <= i < len(s) and 'H' <= s[i] <= 'e':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result