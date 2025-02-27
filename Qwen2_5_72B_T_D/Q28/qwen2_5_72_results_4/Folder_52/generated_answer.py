def return_nth_smallest_ascii(s):
    substring = s[46:73]
    filtered_chars = sorted(set(substring))
    if len(filtered_chars) < 15:
        return None
    return filtered_chars[14]