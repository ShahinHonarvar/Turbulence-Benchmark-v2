def return_nth_smallest_ascii(s):
    substring = s[36:80]
    filtered_chars = sorted(set(substring))
    if len(filtered_chars) >= 12:
        return filtered_chars[11]
    return None