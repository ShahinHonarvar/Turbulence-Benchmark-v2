def return_nth_smallest_ascii(s):
    substring = s[24:72]
    filtered_chars = [char for char in substring if char not in substring[24:72]]
    eighth_smallest = sorted(filtered_chars, key=ord)[7]
    return eighth_smallest