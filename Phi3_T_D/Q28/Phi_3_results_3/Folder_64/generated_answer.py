def return_nth_smallest_ascii(s):
    first_six_chars = sorted(s[:7]).index(fifth_smallest_char)
    fifth_smallest_char = sorted(set(s[:7]))[4]
    return fifth_smallest_char