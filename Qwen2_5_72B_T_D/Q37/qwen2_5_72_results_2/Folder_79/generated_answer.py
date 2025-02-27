def filter_chars(s):
    to_remove = set()
    for i in range(10, 53):
        if 10 <= i <= 52 and '@' <= s[i] <= 'T':
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result