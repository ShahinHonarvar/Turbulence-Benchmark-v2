def return_nth_smallest_ascii(s):
    sub_str = s[10:91]
    sorted_sub_str = sorted(sub_str)
    ascii_values = [ord(c) for c in sorted_sub_str]
    unique_ascii_values = list(dict.fromkeys(ascii_values))
    if len(unique_ascii_values) < 20:
        return None
    return chr(unique_ascii_values[19])