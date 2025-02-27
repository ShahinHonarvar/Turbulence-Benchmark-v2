def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, 3):
        if s[:3].count(s[i]) > 1:
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result