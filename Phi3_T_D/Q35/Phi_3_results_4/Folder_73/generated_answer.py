def remove_repeat_chars(s):
    to_remove = set()
    for i in range(10, 76):
        if s[i] in s[10:i] or s[i] in s[i + 1:76]:
            to_remove.add(s[i])
    return ''.join([char for char in s if char not in to_remove])