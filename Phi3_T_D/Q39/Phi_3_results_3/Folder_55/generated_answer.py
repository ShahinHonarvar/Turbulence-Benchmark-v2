def return_n_greatest_chars(s):
    return sorted(list(set(s)), key=lambda c: -ord(c))[0:75]