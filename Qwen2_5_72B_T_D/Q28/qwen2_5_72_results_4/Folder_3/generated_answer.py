def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(25, 46)]
    sorted_chars = sorted(chars)
    return sorted_chars[10]