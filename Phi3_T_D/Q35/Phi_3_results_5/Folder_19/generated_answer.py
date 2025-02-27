def remove_repeat_chars(s):
    check_range = s[1:4]
    unique_chars = {c for c in check_range if check_range.count(c) > 1}
    return ''.join((c for i, c in enumerate(s) if (i < 1 or i > 3) or c not in unique_chars))