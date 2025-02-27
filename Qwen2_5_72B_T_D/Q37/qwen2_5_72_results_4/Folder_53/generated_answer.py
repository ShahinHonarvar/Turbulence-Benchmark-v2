def filter_chars(s):
    to_remove = set()
    for i in range(83, 100):
        if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9':
            if '*' <= s[i] <= 'j':
                to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result