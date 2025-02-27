def return_nth_smallest_ascii(s):
    if len(s) > 14:
        substring = s[:15]
        sorted_chars = sorted(substring)
        return sorted_chars[14]
    return None