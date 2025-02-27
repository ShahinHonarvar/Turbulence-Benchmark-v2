def filter_chars(s):
    target_chars = set('SRQPONMLKJIHGFEDCBAzxwvutsrqponmlkjihgfedcba')
    return ''.join((c for i, c in enumerate(s) if i < 41 or i > 86 or c not in target_chars))