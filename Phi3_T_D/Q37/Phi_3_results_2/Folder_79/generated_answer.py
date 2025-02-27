def filter_chars(s):
    target_range = set(s[10:53])
    to_remove = {chr(code) for code in range(ord('@'), ord('T') + 1)}
    new_string = ''.join((char for char in s if char not in target_range & to_remove and char not in target_range - to_remove))
    return new_string