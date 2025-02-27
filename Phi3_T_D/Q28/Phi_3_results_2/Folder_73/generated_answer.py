def return_nth_smallest_ascii(s):
    filtered_chars = sorted(set(s[:70]))
    return filtered_chars[9] if len(filtered_chars) > 9 else None