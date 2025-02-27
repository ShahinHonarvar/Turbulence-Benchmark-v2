def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('&'), ord('v') + 1) if 12 <= i <= 88}
    return ''.join((c for c in s if c not in to_remove))