def filter_chars(s):
    to_remove = set()
    for i in range(421, 854):
        if 'D' < s[i] < 'J':
            to_remove.add(s[i])
    result = [ch for ch in s if ch not in to_remove]
    return ''.join(result)