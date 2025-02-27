def filter_chars(s):
    to_remove = set()
    for i in range(42, 93):
        if '0' <= s[i] <= '9' or 'A' <= s[i] <= 'Z' or 'a' >= s[i] >= '/':
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result