def remove_repeat_chars(s):
    char_to_remove = [s[i] for i in range(3, 6) if s.count(s[i]) > 1 and 3 <= i < 6]
    for char in char_to_remove:
        s = s.replace(char, '')
    return s