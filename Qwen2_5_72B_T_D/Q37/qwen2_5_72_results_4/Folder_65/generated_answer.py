def filter_chars(s):

    def should_remove(c):
        return '0' <= c <= '@'
    remove_chars = set((c for c in s[61:71] if should_remove(c)))
    return ''.join((c for c in s if c not in remove_chars))