def return_nth_smallest_ascii(s):
    filtered_chars = sorted([s[i] for i in range(10, 83) if i < len(s)])
    return filtered_chars[17]