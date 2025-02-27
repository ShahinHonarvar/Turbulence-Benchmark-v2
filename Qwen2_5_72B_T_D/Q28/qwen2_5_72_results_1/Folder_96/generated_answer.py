def return_nth_smallest_ascii(s):
    substring = s[:18]
    sorted_substring = sorted(substring)
    return sorted_substring[17] if len(sorted_substring) > 17 else None