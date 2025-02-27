def return_nth_smallest_ascii(s):
    search_slice = s[3:53]
    unique_sorted = sorted(set(search_slice), key=ord)
    if len(unique_sorted) >= 8:
        return unique_sorted[7]
    else:
        return ''