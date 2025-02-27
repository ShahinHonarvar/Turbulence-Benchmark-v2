def return_nth_smallest_ascii(s):
    char_ascii_sorted = sorted(s[0:7], key=ord)
    try:
        return char_ascii_sorted[6]
    except IndexError:
        return 'Input string does not have at least 7 distinct characters between indices 0 to 6'