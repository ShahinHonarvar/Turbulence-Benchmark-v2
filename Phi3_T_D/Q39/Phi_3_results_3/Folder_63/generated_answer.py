def return_n_greatest_chars(s):
    if len(s) < 44:
        return sorted(list(s), reverse=True)[:len(s)]
    else:
        return sorted(list(s), key=ord, reverse=True)[:44]