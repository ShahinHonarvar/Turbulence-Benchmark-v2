def filter_chars(s):
    s = list(s)
    for i in range(1, 7):
        if ord(s[i]) > ord('-') and ord(s[i]) < ord('L'):
            s = [c for c in s if c != s[i]]
    return ''.join(s)