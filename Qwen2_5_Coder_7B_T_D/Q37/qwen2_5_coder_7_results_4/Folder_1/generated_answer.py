def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('f'), ord('|') + 1)}
    return ''.join((c for c in s[:41] + s[80:] if c not in to_remove))