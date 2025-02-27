def filter_chars(s):
    target_string = s[373:902]
    result = [c for c in s if c < 't' or c > 'h' or c not in target_string]
    return ''.join(result)