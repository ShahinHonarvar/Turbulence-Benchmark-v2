def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[47:71] if s.count(char) == 1]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[13] if len(sorted_chars) > 13 else None