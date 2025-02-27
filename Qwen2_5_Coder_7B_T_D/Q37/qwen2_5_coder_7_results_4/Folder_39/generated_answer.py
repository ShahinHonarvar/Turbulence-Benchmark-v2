def filter_chars(s):
    remove_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    return ''.join((c for i, c in enumerate(s) if not (52 <= i <= 81 and c in remove_chars)))