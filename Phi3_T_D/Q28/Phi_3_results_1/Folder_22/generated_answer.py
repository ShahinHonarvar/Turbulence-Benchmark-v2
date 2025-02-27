def return_nth_smallest_ascii(s):
    if len(s) < 17:
        return None
    slice = sorted(s[:17])
    return slice[16] if len(slice) > 0 else None