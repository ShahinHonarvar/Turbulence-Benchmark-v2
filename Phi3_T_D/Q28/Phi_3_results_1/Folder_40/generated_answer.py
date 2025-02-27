def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return None
    first_five = sorted((s[i] for i in range(5)))
    return first_five[4]