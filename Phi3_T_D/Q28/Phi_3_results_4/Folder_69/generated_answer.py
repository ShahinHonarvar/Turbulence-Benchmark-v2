def return_nth_smallest_ascii(s):
    substring = s[67:78]
    distinct_chars = sorted(set(substring))
    nth_smallest = distinct_chars[6] if len(distinct_chars) > 6 else None
    return nth_smallest