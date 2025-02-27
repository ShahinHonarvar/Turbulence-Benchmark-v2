def filter_chars(s):
    target_chars = {s[i] for i in range(42, 93) if '/' <= s[i] <= 'a'}
    return ''.join((c for c in s if c not in target_chars))