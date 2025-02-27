def return_nth_smallest_ascii(s):
    chars = [s[i] for i in range(10)]
    chars.sort(key=ord)
    return chars[9]