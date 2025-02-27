def return_nth_smallest_ascii(s):
    start, end = (51, 89)
    selected_chars = sorted(set(s[start:end + 1]))
    if len(selected_chars) >= 14:
        return selected_chars[13]
    else:
        return None