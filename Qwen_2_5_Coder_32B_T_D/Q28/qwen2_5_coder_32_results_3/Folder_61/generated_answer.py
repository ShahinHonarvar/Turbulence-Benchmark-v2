def return_nth_smallest_ascii(s):
    return sorted(s[:10])[9] if len(s) > 9 else sorted(s)[9]