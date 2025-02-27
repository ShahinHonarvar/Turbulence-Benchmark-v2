def filter_chars(s):
    start, end = (55, 80)
    to_remove = ''.join(sorted(set(s[start:end]).difference(map(chr, range(ord('S'), ord('s') + 1)))))
    return s.replace(to_remove, '')