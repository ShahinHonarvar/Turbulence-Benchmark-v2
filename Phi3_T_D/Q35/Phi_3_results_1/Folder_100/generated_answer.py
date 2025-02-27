def remove_repeat_chars(s):
    target_chars = set(s[44:78])
    new_s = ''.join((char for i, char in enumerate(s) if char not in target_chars or all((s[j] != char for j in range(44, 78) if j != i))))
    return new_s