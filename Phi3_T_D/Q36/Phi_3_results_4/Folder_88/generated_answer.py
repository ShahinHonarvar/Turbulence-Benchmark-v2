def filter_chars(s):
    chars_to_filter = set(chr((ord('S') + 1) % 256) + chr((ord('[') - 1) % 256))
    altered_s = ''.join([c for i, c in enumerate(s) if (i < 78 or i > 81) or c in chars_to_filter or c not in chars_to_filter])
    return altered_s