def filter_chars(s):
    t = ''.join(set(s[18:95]) & set((chr(x) for x in range(ord('L'), ord('a')))))
    return ''.join((c for c in s if c not in t))