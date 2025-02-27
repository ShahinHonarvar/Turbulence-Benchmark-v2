def filter_chars(s):
    return ''.join((c for i, c in enumerate(s) if not (770 <= i <= 970 and ' ' - 'D' >= c >= '-')))