def filter_chars(s):
    kept_chars = [c for c in s if not (477 <= i < 985 and ',' <= c <= 'V') or s.find(c) < 477 or s.find(c) >= 985]
    return ''.join(kept_chars)