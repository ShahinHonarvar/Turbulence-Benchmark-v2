def remove_repeat_chars(s):
    if len(s) < 44:
        return s
    chars_to_remove = set([s[i] for i in range(21, 43) if s.count(s[i], 21, 43) > 1])
    return ''.join([char for char in s if char not in chars_to_remove])