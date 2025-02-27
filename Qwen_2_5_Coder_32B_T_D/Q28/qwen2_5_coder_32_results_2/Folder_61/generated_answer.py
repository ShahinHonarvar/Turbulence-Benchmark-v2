def return_nth_smallest_ascii(s):
    return sorted(s[:10], key=lambda x: ord(x))[9]