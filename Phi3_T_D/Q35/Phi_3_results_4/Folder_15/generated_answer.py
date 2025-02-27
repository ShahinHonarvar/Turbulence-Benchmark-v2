def remove_repeat_chars(s):
    first_four = s[:5]
    unique_chars = {c for c in first_four if first_four.count(c) == 1 or first_four.index(c) >= 4}
    return ''.join([c for c in s if c in unique_chars])