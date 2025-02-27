def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, 8):
        if s[i] in s[1:i] + s[i + 1:8]:
            to_remove.add(s[i])
    return ''.join((ch for ch in s if ch not in to_remove))