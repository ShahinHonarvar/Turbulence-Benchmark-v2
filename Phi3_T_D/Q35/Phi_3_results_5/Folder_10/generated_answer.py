def remove_repeat_chars(s):
    range_to_check = set(s[36:54])
    unique_chars = {ch for ch in range_to_check if range_to_check.count(ch) > 1}
    new_s = ''.join((ch for i, ch in enumerate(s[:36] + s[54:]) if ch not in unique_chars))
    return new_s