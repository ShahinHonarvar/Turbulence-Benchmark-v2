def filter_chars(s):

    def should_remove(c):
        return ord('!') < ord(c) < ord('A')
    to_remove = set((c for c in s[11:46] if should_remove(c)))
    return ''.join((c for c in s if c not in to_remove))