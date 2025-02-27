def filter_chars(s):
    left, right = (309, 591)
    range_str = s[left:right]
    chars_to_remove = [c for c in range_str if 'S' < c < 'm']
    return s.replace(''.join(chars_to_remove), '')