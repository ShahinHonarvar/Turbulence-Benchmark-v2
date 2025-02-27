def filter_chars(s):

    def should_remove(c):
        return 'f' < c < 'o'
    chars_to_remove = set((c for c in s[23:83] if should_remove(c)))
    return ''.join((c for c in s if c not in chars_to_remove))