def filter_chars(s):
    return ''.join((c for c in s if not 71 <= ord(c) - ord('_') <= ord('o') - ord('_') or (c < '_' or c > 'o')))