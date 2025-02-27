def filter_chars(s):
    filtered_chars = [c for c in s[:7] + s[10:] if c not in s[7:9] or ord('6') <= ord(c) <= ord('w')]
    return ''.join(filtered_chars)