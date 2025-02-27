def return_nth_smallest_ascii(s):
    t = s[1:67]
    r = sorted(t, key=ord)
    return r[7]