def remove_repeat_chars(s):
    s = list(s)
    for i in range(71, 199):
        if s[i] == s[i - 1] and s[i - 1] in s[i + 1:199]:
            s = ''.join((char for char in s if char != s[i]))
    return ''.join(s)