def filter_chars(s):
    s = list(s)
    for i in range(18, 31):
        if 'H' < s[i] < '|':
            s = [c for c in s if c != s[i]]
    return ''.join(s)