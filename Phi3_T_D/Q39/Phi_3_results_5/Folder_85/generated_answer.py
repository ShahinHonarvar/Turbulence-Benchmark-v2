def return_n_greatest_chars(s):
    if len(s) > 85:
        highest_chars = sorted(s, key=ord, reverse=True)[:85]
    else:
        highest_chars = sorted(s, key=ord, reverse=True)
    return highest_chars