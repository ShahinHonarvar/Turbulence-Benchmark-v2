def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('K'), ord('m') + 1)))
    return ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 722 or s.index(c) > 832))