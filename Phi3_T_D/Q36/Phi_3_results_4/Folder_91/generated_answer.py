def filter_chars(s):
    for i in range(3):
        char = s[i]
        if char > '$' and char < '?':
            s = s.replace(char, '')
    return s