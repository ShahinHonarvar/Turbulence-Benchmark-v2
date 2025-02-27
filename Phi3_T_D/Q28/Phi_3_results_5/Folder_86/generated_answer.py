def return_nth_smallest_ascii(s):
    target_slice = s[44:69 + 1]
    return sorted(target_slice, key=lambda x: ord(x))[14]