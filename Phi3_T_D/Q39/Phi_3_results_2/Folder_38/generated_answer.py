def return_n_greatest_chars(s):
    top_45_chars = sorted(set(s), reverse=True)[:45]
    return top_45_chars