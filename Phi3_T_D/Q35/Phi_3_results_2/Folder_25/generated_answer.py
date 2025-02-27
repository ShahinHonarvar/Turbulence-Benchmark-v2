def remove_repeat_chars(s):
    altered_s = list(s)
    for i in range(37, 43):
        if altered_s.count(s[i]) > 1:
            altered_s = ''.join([char for char in altered_s if char != s[i]])
    return ''.join(altered_s)