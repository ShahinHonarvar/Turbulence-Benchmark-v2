def return_nth_smallest_ascii(s):
    filtered_chars = [char for i, char in enumerate(s) if 9 <= i <= 59]
    sixth_smallest_ascii = sorted(filtered_chars, key=ord)[5]
    return sixth_smallest_ascii