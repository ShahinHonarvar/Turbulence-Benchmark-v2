def filter_chars(s):
    to_remove = set()
    for i in range(58, 82):
        if 'F' < s[i] < 'O':
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result