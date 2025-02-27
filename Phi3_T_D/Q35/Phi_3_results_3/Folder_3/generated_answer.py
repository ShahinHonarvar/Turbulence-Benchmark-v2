def remove_repeat_chars(s):
    s = list(s)
    for i in range(58, 87):
        char = s[i]
        if s[i:].count(char) > 1:
            s = [x for x in s if x != char]
    return ''.join(s)