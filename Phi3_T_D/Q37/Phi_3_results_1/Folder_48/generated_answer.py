def filter_chars(s):
    target_range = s[513:878]
    filtered_chars = ''.join((c for c in target_range if '?' <= c <= 'n'))
    start = s[:513] + filtered_chars + s[878:]
    return start