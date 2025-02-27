def return_nth_smallest_ascii(s):
    eligible_chars = s[34:86]
    distinct_chars = sorted(set(eligible_chars), key=ord)
    return distinct_chars[19] if len(distinct_chars) > 19 else None