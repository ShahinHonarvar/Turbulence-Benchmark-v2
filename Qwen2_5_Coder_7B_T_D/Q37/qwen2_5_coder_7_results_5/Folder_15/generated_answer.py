def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('?'), ord('f') + 1)}
    return ''.join((c for c in s if c not in to_remove if 2 <= (i := s.index(c)) <= 6))