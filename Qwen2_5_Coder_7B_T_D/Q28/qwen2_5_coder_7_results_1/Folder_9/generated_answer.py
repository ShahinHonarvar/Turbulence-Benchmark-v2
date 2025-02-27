def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(10, 91) if i < len(s)])[19]