def filter_chars(s):
    to_remove = [c for c in s[1:6] if '$' <= c <= ';']
    out_str = ''.join((c for c in s if not c in to_remove))
    return out_str