def return_nth_smallest_ascii(s):
    start = 3
    end = 26
    subset = s[start:end + 1]
    ascii_values = sorted(set(map(ord, subset)))
    if len(ascii_values) < 5:
        return None
    return chr(ascii_values[4])