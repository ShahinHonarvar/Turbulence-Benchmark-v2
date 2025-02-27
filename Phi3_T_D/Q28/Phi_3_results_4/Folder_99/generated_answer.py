def return_nth_smallest_ascii(s):
    target_chars = [s[i] for i in range(17, 66)]
    sorted_chars = sorted(target_chars)
    return sorted_chars[7]