def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(25, 65) if i < len(s)]
    sixth_smallest = sorted(filtered_chars)[5]
    return sixth_smallest