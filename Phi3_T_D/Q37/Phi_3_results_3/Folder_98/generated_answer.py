def filter_chars(s):
    search_range = s[8:10]
    chars_to_remove = [c for c in search_range if 'R' <= c <= 't']
    distilled_string = ''.join((c for c in s if c not in chars_to_remove))
    return distilled_string