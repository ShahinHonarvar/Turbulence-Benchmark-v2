def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[44:70] if s.count(char) == 1]
    sorted_chars = sorted(filtered_chars)
    if len(sorted_chars) < 15:
        return None
    return sorted_chars[14]