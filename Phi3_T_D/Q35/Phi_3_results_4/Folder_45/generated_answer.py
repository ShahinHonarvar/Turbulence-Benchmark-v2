def remove_repeat_chars(s):
    to_remove = set([s[i] for i in range(40, 200) if s.count(s[i]) > 1])
    return ''.join([char for char in s if char not in to_remove])