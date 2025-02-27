def filter_chars(s):
    for i in range(323, 526):
        char = s[i]
        if ord(')') < ord(char) < ord('O'):
            s = s.replace(char, '')
    return s