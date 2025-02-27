def return_nth_smallest_ascii(s):
    candidates = sorted(set(s[40:61]))
    return candidates[18] if len(candidates) >= 19 else None