def remove_repeat_chars(s):
    return ''.join((c for i, c in enumerate(s[:10]) if s[:10].count(c) == 1 or s.find(c, 10) != -1))