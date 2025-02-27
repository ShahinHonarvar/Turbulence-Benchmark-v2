def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda c: ord(c), reverse=True)
    if len(string) >= 2:
        return sorted_chars[:2]
    else:
        return sorted_chars