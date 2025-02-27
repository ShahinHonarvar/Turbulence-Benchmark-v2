def return_nth_smallest_ascii(s):
    substring = s[32:86]
    distinct_chars = sorted(set(substring))
    if len(distinct_chars) < 13:
        return None
    return distinct_chars[12]