def remove_repeat_chars(s):
    target_chars = [s[i] for i in range(44, 78) if s[i] in s[45:77] and s[i] != s[i - 1] and (i != 44)]
    for char in target_chars:
        s = s.replace(char, '')
    return s