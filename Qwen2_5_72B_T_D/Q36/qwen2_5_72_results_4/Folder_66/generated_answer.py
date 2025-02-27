def filter_chars(s):
    to_remove = set()
    for i in range(39, 87):
        if '!' < s[i] < '}':
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result