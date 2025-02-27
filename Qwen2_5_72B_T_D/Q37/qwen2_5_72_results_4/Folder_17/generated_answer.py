def filter_chars(s):
    to_remove = set()
    for i in range(27, 30):
        if 'a' <= s[i] <= 'b' or ';' <= s[i] <= '<':
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result