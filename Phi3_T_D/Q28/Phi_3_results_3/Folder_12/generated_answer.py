def return_nth_smallest_ascii(s):
    valid_chars = [s[i] for i in range(3, 27)]
    valid_chars.sort(key=ord)
    return valid_chars[4]