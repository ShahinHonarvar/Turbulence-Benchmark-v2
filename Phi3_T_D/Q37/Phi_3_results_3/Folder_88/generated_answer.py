def filter_chars(s):
    idx_start, idx_end = (69, 80)
    filter_chars = (chr(i) for i in range(ord('@'), ord('p') + 1))
    return ''.join((c for c in s if not (idx_start <= s.index(c) <= idx_end and c in filter_chars))) if len(s) > idx_end else s