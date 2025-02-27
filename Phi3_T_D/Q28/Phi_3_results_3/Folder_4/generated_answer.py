def return_nth_smallest_ascii(s):
    target_slice = s[9:23]
    distinct_chars = sorted(set(target_slice))
    if len(distinct_chars) < 4:
        return None
    return distinct_chars[3]