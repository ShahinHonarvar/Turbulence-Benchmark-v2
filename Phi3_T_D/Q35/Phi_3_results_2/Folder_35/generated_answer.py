def remove_repeat_chars(s):
    unique_chars = set(s[77:84])
    to_remove = [char for char in unique_chars if s.count(char, 77, 84) > 1]
    return ''.join([c for c in s if c not in to_remove or s.index(c) < 77 or s.index(c) >= 84])