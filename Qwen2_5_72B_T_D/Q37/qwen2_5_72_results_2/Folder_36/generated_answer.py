def filter_chars(s):
    to_remove = set()
    for i in range(259, 503):
        if 259 <= i <= 502 and ',' <= s[i] <= '3':
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result