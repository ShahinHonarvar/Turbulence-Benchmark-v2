def filter_chars(s):
    to_remove = set()
    for i in range(83, 100):
        if 'a' <= s[i] <= 'j' or '*' <= s[i] <= '/':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result