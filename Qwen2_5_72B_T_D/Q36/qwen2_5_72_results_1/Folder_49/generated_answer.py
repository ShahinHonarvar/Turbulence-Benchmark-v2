def filter_chars(s):

    def should_remove(c):
        return 46 < ord(c) < 91 and 'D' < c < 'H'
    return ''.join((c for c in s if not should_remove(c)))