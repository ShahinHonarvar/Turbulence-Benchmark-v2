def remove_repeat_chars(s):
    s = list(s)
    for i in range(10, 100):
        if s[i] in s[i + 1:100]:
            s = ''.join((c for c in s if c != s[i]))
    return ''.join(s)