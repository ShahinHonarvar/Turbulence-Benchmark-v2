def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(60, 89) if i < len(s)])[6]