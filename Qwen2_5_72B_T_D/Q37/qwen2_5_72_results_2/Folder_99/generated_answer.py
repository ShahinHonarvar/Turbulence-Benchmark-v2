def filter_chars(s):
    to_remove = set()
    for i in range(373, 902):
        if 373 <= i <= 901 and 'T' <= s[i] <= 'h':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result