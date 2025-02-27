def return_nth_smallest_ascii(s):
    unique_chars = sorted(set(s[:12]))
    if len(unique_chars) >= 12:
        return unique_chars[11]
    else:
        return None