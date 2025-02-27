def return_nth_smallest_ascii(s):
    if len(s) < 7:
        return None
    substring = s[:7]
    sorted_substring = sorted(substring)
    return sorted_substring[6]