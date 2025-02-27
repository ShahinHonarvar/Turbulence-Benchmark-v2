def filter_chars(s):
    chars_to_remove = {chr(c) for c in range(ord('Q'), ord('i') + 1)}
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 603 or s.index(c) > 759))