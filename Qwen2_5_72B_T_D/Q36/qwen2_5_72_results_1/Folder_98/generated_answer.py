def filter_chars(s):

    def should_remove(c):
        return '1' < c < 'J'
    mid_section = s[4:8]
    chars_to_remove = set((c for c in mid_section if should_remove(c)))
    return ''.join((c for c in s if c not in chars_to_remove))