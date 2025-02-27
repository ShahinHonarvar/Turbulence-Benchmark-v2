def return_nth_smallest_ascii(s):
    sub_slices = [s[i:i + 1] for i in range(12, min(88, len(s)))]
    if len(sub_slices) < 17:
        return None
    return sorted(sub_slices, key=ord)[16]