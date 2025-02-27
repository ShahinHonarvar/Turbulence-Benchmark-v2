def return_nth_smallest_ascii(s):
    substring = s[:15]
    sorted_substring = sorted(substring)
    return sorted_substring[14]