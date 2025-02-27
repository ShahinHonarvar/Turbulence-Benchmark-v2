def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return None
    substring = s[:5]
    sorted_substring = sorted(substring)
    return sorted_substring[3]