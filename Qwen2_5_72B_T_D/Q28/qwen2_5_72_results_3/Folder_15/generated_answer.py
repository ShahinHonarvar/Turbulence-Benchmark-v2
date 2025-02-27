def return_nth_smallest_ascii(s):
    substring = s[:6]
    sorted_substring = sorted(substring)
    return sorted_substring[5]