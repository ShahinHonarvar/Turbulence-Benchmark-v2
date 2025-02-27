def return_nth_smallest_ascii(s):
    filtered_chars = [char for char in s[33:86] if s.count(char) == 1]
    sorted_chars = sorted(filtered_chars, key=ord)
    if len(sorted_chars) >= 13:
        return sorted_chars[12]
    return None