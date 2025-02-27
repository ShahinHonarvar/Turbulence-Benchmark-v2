def return_nth_smallest_ascii(s):
    filtered_chars = sorted(set(s[25:65]))
    if len(filtered_chars) >= 6:
        return filtered_chars[5]
    else:
        return None