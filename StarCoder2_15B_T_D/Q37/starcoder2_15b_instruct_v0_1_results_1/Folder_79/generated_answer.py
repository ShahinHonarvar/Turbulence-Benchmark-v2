def filter_chars(s):
    return ''.join((c for c in s if not 10 <= ord(c) - ord('@') <= 42))