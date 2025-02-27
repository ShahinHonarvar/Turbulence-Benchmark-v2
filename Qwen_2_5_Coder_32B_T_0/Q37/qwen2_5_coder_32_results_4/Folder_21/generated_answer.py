def filter_chars(s):
    if len(s) < 760:
        return s
    chars_to_remove = set(s[603:760]) & set((chr(i) for i in range(ord('Q'), ord('h') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove))