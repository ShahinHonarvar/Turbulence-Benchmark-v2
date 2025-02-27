def remove_repeat_chars(s):
    front_slice = s[:36]
    mid_slice = s[36:54]
    back_slice = s[54:]
    seen = set()
    result_mid = ''.join((c for c in mid_slice if c not in seen or seen.add(c) is None))
    return front_slice + result_mid + back_slice