def filter_chars(s):
    chars_to_filter = set('abcdefghijklmnopqrstuvwxyz@')
    return ''.join((c for c in s if (c < 'A' or c > 'Z') and (c < '0' or c > '9') and (c < '@' or c > 'p') and (69 <= ord(c) <= 80)))