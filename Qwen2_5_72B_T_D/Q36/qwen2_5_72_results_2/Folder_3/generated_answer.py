def filter_chars(s):

    def should_remove(c):
        return 42 < ord(c) < 78 and ord('!') < ord(c) < ord('?')
    return ''.join([c for i, c in enumerate(s) if not (42 < i < 78 and should_remove(c)) or s.count(c) == 0])