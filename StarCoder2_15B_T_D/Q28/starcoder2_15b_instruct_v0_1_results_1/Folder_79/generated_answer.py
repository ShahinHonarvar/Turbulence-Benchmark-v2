def return_nth_smallest_ascii(string: str) -> str:
    substring = string[13:36]
    sorted_substring = sorted(substring)
    return sorted_substring[17]