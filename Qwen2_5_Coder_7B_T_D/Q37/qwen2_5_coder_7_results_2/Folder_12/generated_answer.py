def filter_chars(s):
    filtered_chars = set('FGHIJklmno')
    return ''.join((c for c in s if s.index(c) < 19 or s.index(c) > 90 or c not in filtered_chars))