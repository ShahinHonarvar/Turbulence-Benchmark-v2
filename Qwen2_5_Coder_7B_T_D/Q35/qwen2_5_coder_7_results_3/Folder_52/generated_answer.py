def remove_repeat_chars(s):
    s = list(s)
    repeat_chars = set()
    for i in range(39, 81):
        if s[i] in repeat_chars:
            s[i] = ''
        elif s[i] in s[:38] + s[81:]:
            repeat_chars.add(s[i])
    return ''.join(s)