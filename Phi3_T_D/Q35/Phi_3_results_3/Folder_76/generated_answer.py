def remove_repeat_chars(s):
    unique_chars = set(s[330:544])
    for char in unique_chars:
        s = s.replace(char, '') if s.count(char) > 1 and 330 < s.index(char) < 543 else s
    return s