def return_nth_smallest_ascii(s):
    return sorted([s[i] for i in range(60, 89) if s[i] in s])[6]