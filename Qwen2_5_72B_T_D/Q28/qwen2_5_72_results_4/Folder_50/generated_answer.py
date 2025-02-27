def return_nth_smallest_ascii(s):
    substring = s[25:89]
    filtered_chars = sorted(set(substring))
    if len(filtered_chars) < 11:
        return None
    return filtered_chars[10]