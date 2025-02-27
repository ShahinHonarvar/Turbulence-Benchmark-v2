def return_nth_smallest_ascii(s):
    all_chars = sorted(set(s[40:61]))
    if len(all_chars) >= 19:
        return all_chars[18]
    return None