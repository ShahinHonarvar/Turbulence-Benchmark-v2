def return_nth_smallest_ascii(string):
    substring = string[3:53]
    sorted_substring = sorted(substring)
    return sorted_substring[7]