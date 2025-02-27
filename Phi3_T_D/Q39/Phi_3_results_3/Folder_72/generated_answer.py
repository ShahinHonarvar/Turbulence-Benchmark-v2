def return_n_greatest_chars(string):
    greatest_chars = sorted(string, reverse=True)[:37]
    return greatest_chars