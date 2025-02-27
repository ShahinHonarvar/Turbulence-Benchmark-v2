def filter_chars(s):

    def should_remove(c):
        return 86 < ord(c) < 93 and 'E' < c < '~'
    to_remove = {c for c in s if should_remove(c)}
    return ''.join((c for c in s if c not in to_remove))