def filter_chars(s):
    target_chars = set('MNOPQRSTUV')
    return ''.join((c for i, c in enumerate(s) if (i < 379 or i > 898) or c not in target_chars))