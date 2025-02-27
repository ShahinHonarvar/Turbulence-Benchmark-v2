def filter_chars(s):
    exclude_set = {chr(code) for code in range(ord('g'), ord('|'))}
    return ''.join((c for i, c in enumerate(s) if i not in range(55, 66) or c not in exclude_set))