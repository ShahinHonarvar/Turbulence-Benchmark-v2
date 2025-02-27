def remove_repeat_chars(s):
    to_remove = set()
    for i in range(90, 97):
        if s.count(s[i]) > 1:
            to_remove.add(s[i])
    return ''.join([char for char in s if char not in to_remove])