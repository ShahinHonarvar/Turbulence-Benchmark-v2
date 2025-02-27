def return_nth_smallest_ascii(s):
    subset = [s[i] for i in range(48, 77) if i < len(s)]
    subset.sort(key=lambda x: ord(x))
    return subset[4]