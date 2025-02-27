def remove_repeat_chars(s):
    target_chars = [s[i] for i in range(62, 96) if s.count(s[i], 62, 96) > 1]
    for char in set(target_chars):
        s = s.replace(char, '')
    return s