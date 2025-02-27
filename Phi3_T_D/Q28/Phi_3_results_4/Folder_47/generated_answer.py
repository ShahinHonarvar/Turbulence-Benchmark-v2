def return_nth_smallest_ascii(s):
    index_range = s[3:53]
    n = 8
    return sorted(index_range, key=lambda x: ord(x))[n - 1]