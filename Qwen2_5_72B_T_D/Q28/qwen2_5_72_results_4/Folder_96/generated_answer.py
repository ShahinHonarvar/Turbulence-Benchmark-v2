def return_nth_smallest_ascii(s):
    if len(s) < 18:
        return None
    substring = s[:18]
    sorted_chars = sorted(substring)
    return sorted_chars[17]