def filter_chars(s):
    filter_chars = [c for c in s[26:80] if c <= '<' or c >= '>']
    filter_set = set(filter_chars)
    result = ''.join((c for c in s if c not in filter_set))
    return result