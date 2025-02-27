def return_nth_smallest_ascii(s):
    target_range = s[25:46]
    _, _, _, nth_smallest = sorted(((ord(c), c) for c in target_range))
    if len(target_range) < 11:
        return None
    return nth_smallest