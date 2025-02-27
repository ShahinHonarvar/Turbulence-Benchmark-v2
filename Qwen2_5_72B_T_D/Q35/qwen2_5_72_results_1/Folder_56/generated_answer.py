def remove_repeat_chars(s):
    to_remove = set()
    for i in range(7, 10):
        if s[i] in s[7:10] and s.count(s[i]) > 1:
            to_remove.add(s[i])
    result = ''.join((ch for ch in s if ch not in to_remove))
    return result