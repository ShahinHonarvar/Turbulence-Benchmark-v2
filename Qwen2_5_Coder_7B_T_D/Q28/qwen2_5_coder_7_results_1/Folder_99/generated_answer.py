def return_nth_smallest_ascii(s):
    filtered_chars = [s[i] for i in range(17, 66) if i in range(len(s))]
    sorted_chars = sorted(filtered_chars, key=lambda x: ord(x))
    return sorted_chars[7]