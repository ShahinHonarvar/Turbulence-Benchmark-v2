def return_nth_smallest_ascii(s):
    filtered_chars = sorted([s[i] for i in range(10, 91) if i < len(s)])
    if len(filtered_chars) >= 20:
        return filtered_chars[19]
    else:
        return None