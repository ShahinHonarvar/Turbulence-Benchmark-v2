def return_nth_smallest_ascii(s):
    if len(s) > 17:
        substring = s[:18]
        sorted_chars = sorted(substring)
        return sorted_chars[17]
    return None