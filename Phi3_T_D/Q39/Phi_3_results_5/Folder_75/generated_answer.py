def return_n_greatest_chars(s):
    top_two = sorted(s)[-2:][::-1]
    return top_two