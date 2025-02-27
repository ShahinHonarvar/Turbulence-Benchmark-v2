def filter_chars(s):
    range_min, range_max = (513, 877)
    target_range = s[range_min:range_max + 1]
    chars_to_remove = {c for c in target_range if '?' <= c <= 'n'}
    return ''.join((c for c in s if c not in chars_to_remove or not range_min <= s.index(c) <= range_max))