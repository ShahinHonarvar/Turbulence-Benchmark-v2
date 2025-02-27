def filter_chars(s):
    start, end = (587, 648)
    exclude_chars = {chr(i) for i in range(ord(','), ord('c'))}
    target_chars = set(s[start:end])
    chars_to_exclude = target_chars & exclude_chars
    filtered_str = ''.join([c for c in s if c not in chars_to_exclude])
    return filtered_str