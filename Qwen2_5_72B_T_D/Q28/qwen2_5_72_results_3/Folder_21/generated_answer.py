def return_nth_smallest_ascii(s):
    if len(s) < 66:
        return None
    substring = s[8:66]
    distinct_chars = sorted(set(substring))
    if len(distinct_chars) < 6:
        return None
    return distinct_chars[5]