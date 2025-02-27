def return_nth_smallest_ascii(s):
    relevant_chars = sorted(set(s[1:67]))
    try:
        return relevant_chars[7]
    except IndexError:
        return None