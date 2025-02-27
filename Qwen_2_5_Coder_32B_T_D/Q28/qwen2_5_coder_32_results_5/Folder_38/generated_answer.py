def return_nth_smallest_ascii(s):
    return sorted(s[:46])[-1] if len(s) > 45 else sorted(s)[-1]