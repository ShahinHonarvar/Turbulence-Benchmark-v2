def filter_chars(s):
    to_remove = set()
    for i in range(219, 403):
        if 219 <= i < 403 and '*' < s[i] < '7':
            to_remove.add(s[i])
    result = [ch for ch in s if ch not in to_remove]
    return ''.join(result)