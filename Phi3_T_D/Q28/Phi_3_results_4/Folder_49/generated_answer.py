def return_nth_smallest_ascii(s):
    substr = s[20:81]
    ascii_vals = sorted(map(ord, set(substr)))
    n = 11
    if len(ascii_vals) < n:
        return None
    return chr(ascii_vals[n - 1])