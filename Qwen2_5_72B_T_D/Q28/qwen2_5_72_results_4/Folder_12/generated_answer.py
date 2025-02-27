def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[3:27])
    return filtered_chars[4] if len(filtered_chars) > 4 else None