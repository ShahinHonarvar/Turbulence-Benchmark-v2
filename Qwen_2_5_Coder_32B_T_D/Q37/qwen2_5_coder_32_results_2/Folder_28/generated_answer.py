def filter_chars(s):
    t = set(s[20:80]) & set("!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRST")
    return ''.join((c for c in s if c not in t))