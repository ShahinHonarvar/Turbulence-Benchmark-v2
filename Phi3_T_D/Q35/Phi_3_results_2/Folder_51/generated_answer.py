def remove_repeat_chars(s):
    s = list(s)
    i = 10
    while i > 6:
        count = s[6:i].count(s[i])
        if count > 1:
            s = ''.join((c for c in s if c != s[i]))
        i -= 1
    return ''.join(s)