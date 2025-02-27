def return_nth_smallest_ascii(s):
    filtered_chars = sorted(s[50:60])
    nth = 4
    return filtered_chars[nth] if len(filtered_chars) > nth else None