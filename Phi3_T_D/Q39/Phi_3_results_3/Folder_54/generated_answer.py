def return_n_greatest_chars(s):
    top_n_chars = sorted(s)[-79:][::-1]
    return top_n_chars