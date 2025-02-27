def return_nth_smallest_ascii(s):
    substr_chars = [s[i] for i in range(58, 86)]
    substr_chars.sort(key=ord)
    return substr_chars[18]