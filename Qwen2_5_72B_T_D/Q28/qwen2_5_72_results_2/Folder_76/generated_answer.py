def return_nth_smallest_ascii(s):
    relevant_chars = s[18:67]
    sorted_chars = sorted(relevant_chars)
    return sorted_chars[18]