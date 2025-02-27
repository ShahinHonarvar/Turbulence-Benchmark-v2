def remove_repeat_chars(s):
    target_chars = [c for i, c in enumerate(s[50:91], start=50) if s.count(c) > 1]
    for char in target_chars:
        s = s.replace(char, '')
    return s