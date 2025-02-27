def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[48:77] if s.index(char) >= 48 and s.index(char) <= 76]
    sorted_chars = sorted(filtered_chars)
    return sorted_chars[4] if len(sorted_chars) >= 5 else None