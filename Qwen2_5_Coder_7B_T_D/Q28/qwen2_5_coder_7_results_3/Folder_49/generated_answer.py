def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(20, 81) if i < len(s)])[10]