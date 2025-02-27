def return_nth_smallest_ascii(s):
    sub_s = s[50:77]
    char_sorted = sorted(sub_s, key=lambda c: ord(c))
    return char_sorted[10]