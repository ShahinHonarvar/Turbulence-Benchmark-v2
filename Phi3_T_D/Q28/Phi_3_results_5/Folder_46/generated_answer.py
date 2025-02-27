def return_nth_smallest_ascii(s):
    sub_str = s[34:86]
    distinct_chars = sorted(set(sub_str))
    if len(distinct_chars) < 20:
        return None
    return distinct_chars[19]