def remove_repeat_chars(s):
    idx_range = slice(38, 82)
    for char in set(s[idx_range]):
        s = s.replace(char, '') if s[idx_range].count(char) > 1 else s
    return s