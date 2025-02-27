def return_nth_smallest_ascii(s):
    start, end = (50, 76)
    selected_chars = s[start:end + 1]
    nth_smallest = sorted(selected_chars, key=ord)[10]
    return nth_smallest