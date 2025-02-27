def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(51, 61) if i < len(s)]
    sorted_chars = sorted(chars)
    if len(sorted_chars) < 5:
        return None
    return sorted_chars[4]