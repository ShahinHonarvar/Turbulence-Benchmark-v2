def filter_chars(s):
    if len(s) < 760:
        return s
    exclude = set(s[603:760]) & set((chr(i) for i in range(ord('Q'), ord('i'))))
    return ''.join((c for c in s if c not in exclude))