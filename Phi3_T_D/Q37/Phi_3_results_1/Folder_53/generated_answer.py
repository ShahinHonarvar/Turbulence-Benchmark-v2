def filter_chars(s):
    left_bound, right_bound = (83, 99)
    start_char, end_char = ('*', 'j')
    return ''.join((c for i, c in enumerate(s) if not (left_bound <= i <= right_bound and start_char <= c <= end_char)))