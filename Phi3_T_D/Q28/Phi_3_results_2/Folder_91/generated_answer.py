def return_nth_smallest_ascii(s):
    if s and len(s) >= 8:
        sorted_chars = sorted(s[:8])
        return sorted_chars[7]
    return None