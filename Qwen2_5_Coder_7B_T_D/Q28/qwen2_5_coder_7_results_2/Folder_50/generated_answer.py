def return_nth_smallest_ascii(s):
    sliced = s[25:89]
    sorted_chars = sorted(set(sliced))
    if len(sorted_chars) < 11:
        return None
    return sorted_chars[10]