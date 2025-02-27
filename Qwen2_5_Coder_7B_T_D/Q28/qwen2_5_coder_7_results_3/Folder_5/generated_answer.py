def return_nth_smallest_ascii(s):
    filtered_chars = sorted([s[i] for i in range(5, 90) if i < len(s)])
    return filtered_chars[12]