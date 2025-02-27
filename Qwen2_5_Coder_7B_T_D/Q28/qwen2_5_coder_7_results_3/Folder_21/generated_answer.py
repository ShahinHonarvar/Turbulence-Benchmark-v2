def return_nth_smallest_ascii(s):
    sliced = s[8:66]
    filtered = sorted(filter(lambda x: x.isalpha(), sliced))
    return filtered[5]