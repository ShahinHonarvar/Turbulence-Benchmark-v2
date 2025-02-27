def remove_repeat_chars(s):

    def should_remove(c):
        return 77 <= s.index(c) <= 84 and s[77:84].count(c) > 1
    return ''.join((c for c in s if not should_remove(c)))