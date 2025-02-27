def return_nth_smallest_ascii(s):
    substring = s[:5]
    sorted_substring = sorted(substring)
    return sorted_substring[4]