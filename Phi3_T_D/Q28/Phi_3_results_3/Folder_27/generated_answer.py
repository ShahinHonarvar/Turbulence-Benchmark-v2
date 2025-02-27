def return_nth_smallest_ascii(s):
    eligible_chars = sorted(list(set(s[33:86])))
    if len(eligible_chars) >= 13:
        return eligible_chars[12]
    return None